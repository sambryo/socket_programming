import socket 

server_socket = socket.socket()
server_socket.bind(("127.0.0.1", 3000))
server_socket.listen(5)
(new_socket, address) = server_socket.accept()
message = new_socket.recv(1024)
