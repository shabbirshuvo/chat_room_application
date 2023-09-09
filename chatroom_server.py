import socket
from threading import Thread

# host = '10.11.11.1'
host = '127.0.0.1'
port = 4000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))

clients = {}
addresses = {}


def broadcast(msg, prefix=""):
    for connection in clients:
        connection.send(prefix.encode() + msg)


def handle_client(connection):
    name = connection.recv(1024).decode()
    welcome = "Welcome {}! If you ever want to quit, type quit to exit.".format(name)
    connection.send(welcome.encode())
    msg = "{} has joined the chat".format(name)
    broadcast(msg.encode())
    clients[connection] = name
    while True:
        msg = connection.recv(1024)
        if msg != "quit".encode():
            broadcast(msg, name + ": ")
        else:
            connection.send("quit".encode())
            connection.close()
            del clients[connection]
            broadcast("{} has left the chat".format(name).encode())
            break


def accept_incoming_connections():
    while True:
        connection, address = sock.accept()
        print("{} has connected".format(address))
        connection.send("Welcome to the chatroom".encode())
        addresses[connection] = address
        Thread(target=handle_client, args=(connection,)).start()


if __name__ == '__main__':
    sock.listen(5)
    print("Server listening on port {}".format(port))

    t1 = Thread(target=accept_incoming_connections)
    t1.start()
    t1.join()
