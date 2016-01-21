import socket

UDP_IP = "10.0.0.8"  # Receiver's IP address
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET,  # Internet
                     socket.SOCK_DGRAM)  # UDP
sock.bind((UDP_IP, UDP_PORT))

count = 0
while True:
    data, addr = sock.recvfrom(1024)  # Buffer size is 1024 bytes
    count += 1
    print "received message:", data
    print "packets received:", count
