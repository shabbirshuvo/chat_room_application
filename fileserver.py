import socket

host = 'localhost'
port = 4000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen(1)

print("Server listening on port {}".format(port))
connection, address = sock.accept()
print("Connection from {}".format(address))

file_name = connection.recv(1024)
try:
    file = open(file_name.decode(), 'rb')
    content = file.read()
    connection.send(content)
    file.close()
except FileNotFoundError:
    message = "File not found"
    connection.send(message.encode())