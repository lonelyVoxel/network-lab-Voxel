#!/usr/bin/env python3
"""
    multicast-server.py - UDP server that listens for multicast messages on port 9000 and prints them out.
    Author: Rose/Roxy Lalonde (roseernst@bennington.edu) from template by Andrew Cencini (acencini@bennington.edu)
    Date: 3/4/2020
"""

import socket
import struct

# Defining the address to receive messages and the port on which to receive them through.
MCAST_GRP = "224.1.1.1"
MCAST_PORT = 9000

# Set up the socket on IPv4 and UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Lets go of the socket in event of a crash
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Like always, bind the socket to the port
sock.bind(("", MCAST_PORT))

# This is needed to set up the multicast group. The comments here were long and I didn't quite get it.
mreq = struct.pack("4sl", socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

while 1:
    data, addr = sock.recvfrom(1024)
    print("{0} received: {1}".format(addr[0], data.decode()))
