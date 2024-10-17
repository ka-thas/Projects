#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <netdb.h>

#include "d1_udp.h"

// My imports. Used for waiting for ACK
#include <sys/time.h>
#include <errno.h>

D1Peer *d1_create_client()
{
    int fd;
    struct sockaddr_in server = {0};

    fd = socket(AF_INET, SOCK_DGRAM, 0);
    if (fd < 0)
    {
        perror("socket");
        return NULL;
    }

    D1Peer *client = (D1Peer *)malloc(sizeof(D1Peer));
    if (client == NULL)
    {
        perror("malloc");
        close(fd);
        return NULL;
    }

    client->socket = fd;
    client->addr = server;
    client->next_seqno = 0;

    return client;
}

D1Peer *d1_delete(D1Peer *peer)
{
    if (peer != NULL)
    {
        close(peer->socket);
        free(peer);
    }
    return NULL;
}

int d1_get_peer_info(struct D1Peer *peer, const char *peername, uint16_t server_port)
{
    struct addrinfo hints, *res;
    int rc;

    // Set up hints
    memset(&hints, 0, sizeof(hints));
    hints.ai_family = AF_INET;
    hints.ai_socktype = SOCK_DGRAM;

    // Get address info
    char server_port_str[6];
    sprintf(server_port_str, "%d", server_port);
    rc = getaddrinfo(peername, server_port_str, &hints, &res);
    if (rc != 0)
    {
        fprintf(stderr, "getaddrinfo: %s\n", gai_strerror(rc));
        return 0;
    }

    // Copy address info to peer
    struct sockaddr_in *addr = (struct sockaddr_in *)res->ai_addr;
    peer->addr = *addr;

    freeaddrinfo(res);

    return 1;
}

/* helper function used in recv and send */
uint16_t compute_checksum(char *packet, size_t total_size)
{
    uint8_t odd_checksum = 0;
    uint8_t even_checksum = 0;

    for (size_t i = 0; i < total_size; i++)
    {
        // even i is odd byte
        if (i % 2) // true if i is odd
        {
            even_checksum ^= packet[i];
        }
        else
        {
            odd_checksum ^= packet[i];
        }
    }
    return odd_checksum << 8 | even_checksum;
}

int d1_recv_data(struct D1Peer *peer, char *buffer, size_t sz)
{
    memset(buffer, 0, sz); // clear buffer
    int fd = peer->socket;
    struct sockaddr_in server = peer->addr;
    int rc = 0;
    char *packet = (char *)malloc(sz);
    if (packet == NULL)
    {
        perror("malloc");
        return -1;
    }

    socklen_t addrlen = sizeof(struct sockaddr_in);
    rc = recvfrom(fd, packet, sz, 0, (struct sockaddr *)&server, &addrlen);
    if (rc < 0)
    {
        perror("recvfrom");
        return -1;
    }

    // Decypher header
    struct D1Header header = {0};
    memcpy(&header, packet, sizeof(header));
    header.flags = ntohs(header.flags);
    header.checksum = ntohs(header.checksum);
    header.size = ntohl(header.size);

    // Analyze checksum
    packet[2] = 0;
    packet[3] = 0;
    uint16_t checksum = compute_checksum(packet, rc);
    if (checksum != header.checksum)
    {
        fprintf(stderr, "> Checksum mismatch\n");
        printf("Computed hecksum: %02X\n", checksum);
        printf("Packet checksum: %02X\n", header.checksum);
        d1_send_ack(peer, !(header.flags & SEQNO));
        // return d1_recv_data(peer, buffer, sz);
        return -1;
    }

    // Check size
    if (header.size != (uint32_t)rc)
    {
        fprintf(stderr, "Size mismatch\n");
        d1_send_ack(peer, !(header.flags & SEQNO));
        // return d1_recv_data(peer, buffer, sz);
        return -1;
    }

    // extract buffer
    memcpy(buffer, packet + sizeof(header), rc - sizeof(header));

    d1_send_ack(peer, (header.flags & SEQNO)); // passes 128 as seqno, but evaluates to TRUE

    free(packet);
    return rc;
}

int d1_wait_ack(D1Peer *peer, int ackno)
{
    int fd = peer->socket;
    struct sockaddr_in server = peer->addr;
    int rc = 0;
    char *temp = (char *)malloc(sizeof(struct D1Header));

    socklen_t addrlen = sizeof(struct sockaddr_in);

    // Set the timeout to 1 second
    struct timeval timeout;

    timeout.tv_sec = 1;
    timeout.tv_usec = 0;
    if (setsockopt(fd, SOL_SOCKET, SO_RCVTIMEO, &timeout, sizeof(timeout)) < 0)
    {
        perror("setsockopt");
        free(temp);
        return -1;
    }

    rc = recvfrom(fd, temp, sizeof(D1Header), 0, (struct sockaddr *)&server, &addrlen);
    if (rc < 0)
    {

        if (errno == EWOULDBLOCK || errno == EAGAIN)
        {
            printf("recvfrom timed out\n"); // recvfrom timed out
        }
        else
        {
            perror("recvfrom"); // an error occurred
        }
        free(temp);
        return -1;
    }

    // Checking the received ACK

    struct D1Header header;
    memcpy(&header, temp, sizeof(header));
    header.flags = ntohs(header.flags);
    header.checksum = ntohs(header.checksum);
    header.size = ntohl(header.size);

    // Check flags
    if (!(header.flags & FLAG_ACK))
    {
        fprintf(stderr, "> Not an ACK\n");
        free(temp);
        return -1;
    }

    // check ackno
    if ((header.flags & ACKNO) != ackno)
    {
        fprintf(stderr, "> ACK number mismatch\n");
        free(temp);
        return -1;
    }

    temp[2] = 0;
    temp[3] = 0;

    // Check checksum
    uint16_t checksum = compute_checksum(temp, rc);
    if (checksum != header.checksum)
    {
        fprintf(stderr, "> Checksum mismatch\n");
        printf("Computed hecksum: %02X\n", checksum);
        printf("Packet checksum: %02X\n", header.checksum);
        free(temp);
        return -1;
    }

    // Check size
    if (header.size != (uint32_t)rc)
    {
        fprintf(stderr, "> Size mismatch\n");
        free(temp);
        return -1;
    }

    free(temp);

    return rc;
}

int d1_send_data(D1Peer *peer, char *buffer, size_t sz)
{
    int total_size = sz + sizeof(struct D1Header);
    if (total_size > BUFSIZE)
    {
        fprintf(stderr, "d1_send_data: buffer size too small\n");
        return -1;
    }

    int fd = peer->socket;
    struct sockaddr_in server = peer->addr;
    struct D1Header header = {0};

    // Prepare header
    header.flags = FLAG_DATA;
    int seqno = peer->next_seqno;
    if (seqno)
        header.flags |= SEQNO;
    peer->next_seqno = !peer->next_seqno;

    header.flags = htons(header.flags);
    header.size = htonl(total_size);

    char *packet = (char *)malloc(total_size);
    if (packet == NULL)
    {
        perror("malloc");
        return -1;
    }

    header.checksum = 0;

    memcpy(packet, &header, sizeof(header));
    memcpy(packet + sizeof(header), buffer, sz); // appends buffer

    // Compute checksum
    header.checksum = compute_checksum(packet, total_size);
    header.checksum = htons(header.checksum);
    memcpy(packet, &header, sizeof(header));

    // do-while loop to resend packet if ack not recieved
    do
    {
        sendto(fd, packet, total_size, 0, (struct sockaddr *)&server, sizeof(server));
    } while (d1_wait_ack(peer, seqno) < 0); // blocking call for <= 1 sec

    free(packet);

    return total_size;
}

void d1_send_ack(struct D1Peer *peer, int seqno)
{
    int fd = peer->socket;
    struct sockaddr_in server = peer->addr;
    struct D1Header header = {0};

    header.flags = FLAG_ACK;
    if (seqno)
        header.flags |= ACKNO;
    header.flags = htons(header.flags);
    header.size = htonl(sizeof(struct D1Header));

    char *packet = (char *)malloc(sizeof(struct D1Header));
    if (packet == NULL)
    {
        perror("malloc");
        return;
    }
    header.checksum = 0;

    memcpy(packet, &header, sizeof(header));

    header.checksum = compute_checksum(packet, sizeof(header));
    memcpy(packet, &header, sizeof(header)); // update checksum

    sendto(fd, &header, sizeof(header), 0, (struct sockaddr *)&server, sizeof(server));

    free(packet);
}
