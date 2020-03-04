#!/usr/bin/env python3
"""
    multicast-client.py - UDP client that broadcasts multicast messages on port 9000.
    Author: Rose/Roxy Lalonde (roseernst@bennington.edu) from template by Andrew Cencini (acencini@bennington.edu)
    Date: 3/4/2020
"""

import socket

# Defining the address to send the message to and the port on which to send it through.
MCAST_GRP = "224.1.1.1"
MCAST_PORT = 9000
MESSAGE = "Trans rights!"

# Make the socket with IPv4, but this time for UDP!
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Yeet that data to EVERYONE!
sock.sendto(MESSAGE.encode(), (MCAST_GRP, MCAST_PORT))

# Code for later to potentially control routing
# sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
