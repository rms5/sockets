import socket
import sys

args = len(sys.argv)
#if len(sys.argv) < 2: 
#	exit("An integer command-line argument specifies how many packets to send.")

if args < 2:
	UDP_IP = "10.0.0.8" #defualt receivers ip address
else:
	UDP_IP = str(sys.argv[1]) #receivers ip address
if args < 3:
	UDP_PORT = 5005 # default port
else:
	UDP_PORT = int(sys.argv[2]) #if port passed in.
MESSAGE = "Packet number "

for num in range(1, tosend):
    print "message:", MESSAGE + str(num)

    sock = socket.socket(socket.AF_INET,  # Internet
           socket.SOCK_DGRAM)  # UDP
    sock.sendto(MESSAGE + str(num), (UDP_IP, UDP_PORT))
