#!/usr/bin/env python3
"""
    udp-client.py - UDP client that talks to a remote server on port 9000 and sends a simple message.
    Author: Rose/Roxy Lalonde (roseernst@bennington.edu) from template by Andrew Cencini (acencini@bennington.edu)
    Date: 3/4/2020
"""

import socket

# Defining the address to send the message to and the port on which to send it through.
UDP_ADDRESS = "127.0.0.1"
UDP_PORT = 9000
MESSAGE = "If you or a loved one has been diagnosed with mesothelioma, you may be entitled to financial compensation."

# Make the socket with IPv4, but this time for UDP!
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Sets a timeout of 5 seconds in case the echo is not received.
sock.settimeout(5)

# Yeet that data to the server, and don't look back.
sock.sendto(MESSAGE.encode(), (UDP_ADDRESS, UDP_PORT))
print("Sent message: '{0}' to {1}".format(MESSAGE, UDP_ADDRESS))

# Allows us to receive the echo from the server.
data, addr = sock.recvfrom(1024)
print("{0} received: {1}".format(addr[0], data.decode()))
