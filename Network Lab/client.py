#!/usr/bin/env python3
"""
    client.py - TCP client that talks to a remote server on port 9000 and sends a simple message
    Author: Rose/Roxy Lalonde (roseernst@bennington.edu) from template by Andrew Cencini (acencini@bennington.edu)
    Date: 3/4/2020
    Protocol: Connect -> send string -> disconnect
"""

import socket

# Defining the address to send the message to and the port on which to send it through.
TCP_ADDRESS = '10.10.117.73'
TCP_PORT = 9000
MESSAGE = 'H'

# Time to make the socket! We'll be using IPv4 (first parameter) and TCP.
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the remote IP on a specific port, both of which were specified earlier.
sock.connect((TCP_ADDRESS, TCP_PORT))

# Encode the message into bytes that can be sent over the Internet. Now it's time to send memes >:]
sock.send(MESSAGE.encode())

# End the communication.
sock.close()
