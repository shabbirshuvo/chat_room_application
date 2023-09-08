import socket

host = 'localhost'
port = 4000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen(1)
print("Server listening on port {}".format(port))


connection, address = sock.accept()

message = "There is something important for you"
connection.send(message.encode())
connection.close()