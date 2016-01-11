import socket

UDP_IP = "10.0.0.9"
UDP_PORT = 6666
MESSAGE = "SOS"

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "message:", MESSAGE

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.sendto("SOS", ("10.0.0.9", 6666))
