#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#include "d2_lookup.h"

D2Client *d2_client_create(const char *server_name, uint16_t server_port)
{
    D1Peer *peer = d1_create_client();
    if (peer == NULL)
    {
        return NULL;
    }

    if (d1_get_peer_info(peer, server_name, server_port) < 0)
    {
        d1_delete(peer);
        return NULL;
    }

    // Allocate memory for the D2Client
    D2Client *client = (D2Client *)malloc(sizeof(D2Client));
    if (client == NULL)
    {
        perror("malloc");
        d1_delete(peer);
        return NULL;
    }

    client->peer = peer;
    return client;
}

D2Client *d2_client_delete(D2Client *client)
{
    if (client != NULL)
    {
        d1_delete(client->peer);
        free(client);
    }
    return NULL;
}

int d2_send_request(D2Client *client, uint32_t id)
{
    // Create the request packet
    PacketRequest req = {0};
    req.id = id;
    req.type = TYPE_REQUEST;
    req.id = htonl(req.id);
    req.type = htons(req.type);

    // Send the request packet using d1 abstraction
    if (d1_send_data(client->peer, (char *)&req, sizeof(PacketRequest)) < 0)
    {
        return -1;
    }
    return 1;
}

int d2_recv_response_size(D2Client *client)
{
    char buffer[1024]; // 1 kibiByte buffer

    // Receive the response size packet using d1 abstraction
    if (d1_recv_data(client->peer, buffer, 1000) < 0)
    {
        return -1;
    }
    PacketResponseSize resp;
    memcpy(&resp, buffer, sizeof(PacketResponseSize));

    resp.type = ntohs(resp.type);
    if (resp.type != TYPE_RESPONSE_SIZE)
    {
        return -1;
    }

    resp.size = ntohs(resp.size);

    return resp.size;
}

int d2_recv_response(D2Client *client, char *buffer, size_t sz)
{
    return d1_recv_data(client->peer, buffer, sz);

    /* d1 header is checked in d1_recv_data
     * and d2 header is checked in d2_test_client.c */
}

LocalTreeStore *d2_alloc_local_tree(int num_nodes)
{
    LocalTreeStore *tree = (LocalTreeStore *)malloc(sizeof(LocalTreeStore));
    if (tree == NULL)
    {
        perror("malloc");
        return NULL;
    }

    tree->number_of_nodes = num_nodes;

    // Allocate memory for the array of NetNode pointers
    tree->nodes = (NetNode **)malloc(sizeof(NetNode *) * num_nodes);
    if (tree->nodes == NULL)
    {
        perror("malloc");
        free(tree);
        return NULL;
    }

    // Initialize all the NetNode pointers to NULL
    memset(tree->nodes, 0, sizeof(NetNode *) * num_nodes);

    return tree;
}

void d2_free_local_tree(LocalTreeStore *tree)
{
    if (tree == NULL)
    {
        return;
    }

    for (int i = 0; i < tree->number_of_nodes; i++)
    {
        if (tree->nodes[i] != NULL)
        {
            free(tree->nodes[i]);
        }
    }

    free(tree->nodes);
    free(tree);
}

int d2_add_to_local_tree(LocalTreeStore *nodes_out, int node_idx, char *buffer, int buflen)
{
    if (nodes_out == NULL)
    {
        fprintf(stderr, "nodes_out is NULL\n");
        return -1;
    }

    if (node_idx >= nodes_out->number_of_nodes)
    {
        fprintf(stderr, "node_idx is out of bounds\n");
        return -1;
    }

    if (buffer == NULL)
    {
        fprintf(stderr, "buffer is NULL\n");
        return -1;
    }

    if (buflen <= 0)
    {
        fprintf(stderr, "buflen is <= 0\n");
        return -1;
    }

    /*
    Left this here intentionally to show understanding of the buffer
    I used similar prints in d1 when debugging the checksum

    printf("\n<-- d2_add_to_local_tree [%2X / %d]\n", buflen, buflen);
    printf("buffer in hex: ");
    for (int i = 0; i < buflen; i++)
    {
        if (!((i) % 4))
            printf("\n ");
        printf(" %02X ", (unsigned char)buffer[i]);
    }
    printf("\n"); */

    int offset = 0;
    int num_nodes_in_buffer = 0;
    while (offset < buflen)
    {
        NetNode *pointer = (NetNode *)(buffer + offset);

        NetNode *node = (NetNode *)malloc(sizeof(NetNode));
        if (node == NULL)
        {
            perror("malloc");
            return -1;
        }

        node->id = ntohl(pointer->id);
        node->value = ntohl(pointer->value);
        int num_children = ntohl(pointer->num_children);
        node->num_children = num_children;

        memset(node->child_id, 0, sizeof(node->child_id));

        for (int i = 0; i < num_children; i++)
        {
            node->child_id[i] = ntohl(pointer->child_id[i]);
        }

        nodes_out->nodes[node_idx] = node;

        offset += 12 + 4 * num_children;
        num_nodes_in_buffer++;
        node_idx++;

        if (num_nodes_in_buffer >= 5)
        {
            break;
        }
    }

    return node_idx;
}

void print_tree_recursive(LocalTreeStore *tree, int node_idx, int depth)
{
    if (node_idx >= tree->number_of_nodes)
    {
        return;
    }

    NetNode *node = tree->nodes[node_idx];
    if (node == NULL)
    {
        return;
    }

    char *deapth_str = (char *)malloc(sizeof(char) * (depth * 2 + 1));
    memset(deapth_str, '-', depth * 2);
    deapth_str[depth * 2] = '\0';

    printf("%s id %d value %d children %d\n", deapth_str, node->id, node->value, node->num_children);

    free(deapth_str);

    for (u_int32_t i = 0; i < node->num_children; i++)
    {
        print_tree_recursive(tree, node->child_id[i], depth + 1);
    }
}

void d2_print_tree(LocalTreeStore *nodes_out)
{
    if (nodes_out == NULL)
    {
        fprintf(stderr, "nodes_out is NULL\n");
        return;
    }

    if (nodes_out->nodes == NULL)
    {
        fprintf(stderr, "nodes_out->nodes is NULL\n");
        return;
    }

    print_tree_recursive(nodes_out, 0, 0);
}
