import socket 

client_socket = socket.socket()
client_socket.connect(("127.0.0.1", 3000))
client_socket.sendall("Hello World")
