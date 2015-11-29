#!/usr/bin/env python3
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for n in range(0, 11):
    s.sendto(str(n).encode('ascii'), ('127.0.0.1', 50007))
s.sendto(b'QUIT', ('127.0.0.1', 50007))
s.close()
