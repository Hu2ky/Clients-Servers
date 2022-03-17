import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 27700

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind((bind_ip, bind_port))

print ("[*] UPD_Server Listening on %s:%d" % (bind_ip, bind_port))

# This is the thread we handle the data from  the client

while True:

    client, addr = server.recvfrom(1024)
    print ("[*] Accepted connection from: %s:%d" % (addr[0], addr[1]))
    print (client)
    server.sendto(b"Hello UPD Client", (addr[0], addr[1]))
