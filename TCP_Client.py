
# importing essential libraries for the program
import socket

# variables
target_host = "0.0.0.0"
target_port = 27700

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the client
client.connect((target_host, target_port))

# send data
client.send(b"SYN")

# receive data
response = client.recv(4096)

# printing output
print(response)












