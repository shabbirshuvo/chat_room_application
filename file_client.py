import socket

host = 'localhost'
port = 4000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))

file_name = input("Enter the file name: ")
sock.send(file_name.encode())
read_file = sock.recv(1024)
print(read_file.decode())

sock.close()
