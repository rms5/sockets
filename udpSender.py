import socket
import sys

if len(sys.argv) < 2: 
	exit("An integer command-line argument specifies how many packets to send.")

tosend = int(sys.argv[1])

UDP_IP = "10.0.0.8"  # Receiver's IP address
UDP_PORT = 5005
MESSAGE = "Packet number "

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT

for num in range(1, tosend):
    print "message:", MESSAGE + str(num)

    sock = socket.socket(socket.AF_INET,  # Internet
           socket.SOCK_DGRAM)  # UDP
    sock.sendto(MESSAGE + str(num), (UDP_IP, UDP_PORT))
