import socket

# variables
target_host = "0.0.0.0"
target_port = 27700

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send some data
client.sendto(b"Hi UPD Sever",(target_host,target_port))

# receive some data
data = client.recv(4096)

# printing output
print(data)
