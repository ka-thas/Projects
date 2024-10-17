# HE in general

I probably tested for more parameter errors than necessary. Like `if (buffer = Null) return -1;`.

I hope my variable names and the README is clear enough. as I could've commented more in the code.

The hardest part of the entire exam was the checksum computation.

# 1. D1 UDP

## Create and delete peer

### Create peer

I first malloc a new D1Peer structure and initialize the fields with the parameters. The server address is converted from a string to a sockaddr_in structure using inet_pton. The port number is converted from a string to an integer using atoi (ascii to int). The socket file descriptor (fd) is created using socket().

### Delete peer

I retrieve the socket fd from the struct D1Peer, then close the socket using close() and free the allocated memory for the D1Peer using free().

### get peer info

The getaddrinfo function is used to get the address information of the server. The port number is converted to a string using the sprintf function. The server address and port number are then concatenated and stored in the server_info variable.

## Send data

I retrieve the socket fd and the server address from D1Peer. I then malloc a temp buffer to store the entire data packet. I create a D1Header on the stack and set the flags, calculate the checksum, and size fields of the header. I then memcpy the header into the temp buffer and append the data buffer provided by the parameter into the temp buffer.

I use a do-while loop to send the data packet to the server using sendto(), which resends the packet until I get the correct ack in return from the server.

### Waiting for ACK 

My D1_wait_ack function differs from the intended implementation in that it returns a boolean value and is used as the condition in a while loop. The function waits for an ACK from the server for one second. If an ACK is received, the function returns true. If no ACK is received within the specified time or there is something wrong with the ack, the function returns false.

I'm guessing that the intended implementation was to call wait_ack at the end of send_data, and that wait_ack would call send data in case of failure. I could've used the provided buffer to store the data packet and header, but since I chose to malloc a temp buffer instead I now wanted to minimize the number of times I had to alloc and put toghether the packet.

Since the implementation was non-mandatory, I also decided to change the parameters in the d1_udp.h file.

## Receive data

I clear the buffer using `memset(buffer, 0, sz);` because valgrind kept complaining about uninitialized values in the print statements of d1_test_client.c.

I use my own malloced packet buffer. After controlling the checksum and the size of the packet, I copy the data from the packet buffer to the provided buffer.

Finally, I send an ACK to the server using d1_send_ack()

### Send ACK

Essentially idetical to send_data, but with different flags.

# D2 Lookup

## d2 in general

The hardest part was understanding the structure of the entire task. The HE presentation helped a lot.

This part was easier because a lot of the technical stuff was already implemented and abstracted away in the D1 UDP part.

## Create and delete lookup

### Create client

Creating a d1 peer by calling d1 functions using the parameters. 

Malloc a new D2Lookup structure and assign the peer.

### Delete client

Free the peer and the lookup.

## Send request

Create a PacketRequest structure on the stack and assign the parameters, and the simply call the d1_send_data function.

## Receive response size

Create a PacketResponse structure on the stack and call d1_receive_data. If the response is valid, return the size from the response.

## Receive response

This function solely calls the d1_receive_data function to the provided buffer, which seems wierd to me, but the d1 header is checked in the d1_receive_data function and the d2 header is checked in the d2_test_client.c event loop.

# Tree

## Alloc tree

Mallocs the tree struct. I went with a pointer-to-pointers approach for the tree structure as the .h file said that we should change it to suit my needs. So that array was also malloced based on the num_nodes parameter.

## Free tree

Frees all malloced NetNode structs and the array that held them, and then the tree struct itself.

## Add node to tree

First a bunch of checks to see that all the parameters are valid.

Iterates though every NetNode stored in the buffer and creates a new NetNode Structure for each. This is achieved by assigning a NetNode pointer directly into the buffer and then typecasting the buffer to a NetNode pointer.

This was quite simple as every field of the NetNode struct and the buffer was 4 bytes.

After reading the num_children field, I use a for-loop to assign the ids to the children array of the NetNode struct.

All unused childids of a NetNode is set to zero, but it's known from the handout that only the root will have the ID zero, so it's implied that the id zero cant be a child.

## Printing the tree

I used a recursive function to print the tree. I first print the root node, then I call the function recursively for every child of the root node.

It was a bit tricky to get the formatting right, but I think it turned out okay.

Because the tree's nodes were implemented as an array with corelated indexes, I could use the id as an index to get the NetNode struct efficently.