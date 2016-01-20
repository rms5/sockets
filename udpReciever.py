import socket

UDP_IP = "10.0.0.9"
UDP_PORT = 6666

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind(("10.0.0.9", 6666))

count = 0
while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    count += 1
    print "received message: ", data
    print "packets received: ", count
