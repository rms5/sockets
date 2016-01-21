# If you just call using python udpSendXPackets.py, will default to 1k sends, 10.0.0.8 ip, 5005 as port.
# If you call with multiple args: 
#first arg = packets sent 
#second arg = ip to send to,
#third arg = port.

import socket
import sys

args = len(sys.argv) #get the number of args passed in. This is the list length, the first
					 #item in the list will always be the name.

if args < 2: 
	tosend = 1000
else:
	tosend = int(sys.argv[1])
if args < 3:
	UDP_IP = "10.0.0.8" # default ip address
else:
	UDP_IP = str(sys.argv[2]) #recievers ip address
if args < 4:
	UDP_PORT = 5005 # default port
else:
	UDP_PORT = int(sys.argv[3]) # port to use.
MESSAGE = "Packet number "

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT

for num in range(1, tosend):
    print "message:", MESSAGE + str(num)

    sock = socket.socket(socket.AF_INET,  # Internet
           socket.SOCK_DGRAM)  # UDP
    sock.sendto(MESSAGE + str(num), (UDP_IP, UDP_PORT))
