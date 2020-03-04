#!/usr/bin/env python3
"""
    server.py - TCP server that listens on TCP port 9000 and prints what is sent to it.
    Author: Rose/Roxy Lalonde (roseernst@bennington.edu) from template by Andrew Cencini (acencini@bennington.edu)
    Date: 3/4/2020
"""

import socket

# Set our interface to listen on (all of them), which port to receive on, and how many bytes at a time to read.
TCP_ADDRESS = "0.0.0.0"
TCP_PORT = 9000
BUFFER_SIZE = 20

while 1:
    # Set our socket using IPv4 and TCP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Set the socket to the specified address and port
    sock.bind((TCP_ADDRESS, TCP_PORT))

    # Allows us to listen to incoming connections. The 1 means we'll backlog one connection at a time.
    sock.listen(1)

    # Conn is the connection, and addr is the tuple which represents the IP and port of the client.
    conn, addr = sock.accept()
    print("Connection address: {0}".format(addr[0]))

    # Read incoming data until none is left, then close the connection.
    data = conn.recv(BUFFER_SIZE).decode()
    while data != "":
        print("received data: {0}".format(data))
        data = conn.recv(BUFFER_SIZE).decode()
    conn.close()
