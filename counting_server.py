#!/usr/bin/env python3
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', 50007))
while True:
    (data, address) = s.recvfrom(4096)
    if data == b'QUIT':
        break
    print(data.decode('ascii'))
s.close()
