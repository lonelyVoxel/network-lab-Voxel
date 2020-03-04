#!/usr/bin/env python3
"""
    udp-server.py - UDP server that listens on UDP port 9000 and prints what is sent to it.
    Author: Rose/Roxy Lalonde (roseernst@bennington.edu) from template by Andrew Cencini (acencini@bennington.edu)
    Date: 3/4/2020
"""

import socket

# Set our interface to listen on (all of them), which port to receive on, and how many bytes at a time to read.
UDP_ADDRESS = "127.0.0.1"
UDP_PORT = 9000

# Set up our socket with IPv4 and UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the given address and port
sock.bind((UDP_ADDRESS, UDP_PORT))

while 1:
    data, addr = sock.recvfrom(1024)
    print("{0} received: {1}".format(addr[0], data.decode()))
    sock.sendto(data, addr)  # The echo
