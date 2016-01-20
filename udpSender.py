import socket
import sys

tosend = sys.argv[1]

UDP_IP = "10.0.0.8" #recievers ip address
UDP_PORT = 5005
MESSAGE = "Packet number "

for num in range(1,tosend):

    print "UDP target IP:", UDP_IP
    print "UDP target port:", UDP_PORT
    print "message:", MESSAGE + str(num)

    sock = socket.socket(socket.AF_INET, # Internet
           socket.SOCK_DGRAM) # UDP
    sock.sendto(MESSAGE + str(num), (UDP_IP, UDP_PORT))
