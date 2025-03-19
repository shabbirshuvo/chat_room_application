import socket
import sys
import time
from threading import Thread

# host = '10.11.11.1'
host = '127.0.0.1'
port = 4000

def create_server_socket():
    """Create and configure the server socket with proper options"""
    try:
        # Create the socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Set socket options
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        # Bind the socket
        sock.bind((host, port))
        return sock
    except socket.error as e:
        print(f"\nError creating server socket: {e}")
        print("This might be because:")
        print("1. The port is already in use")
        print("2. You don't have permission to use this port")
        print("3. The address is already in use")
        print("\nTrying to clean up and retry in 5 seconds...")
        
        try:
            sock.close()
        except:
            pass
            
        time.sleep(5)
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            sock.bind((host, port))
            print("Successfully created server socket!")
            return sock
        except socket.error as e:
            print(f"\nFailed to create server socket after retry: {e}")
            print("Please ensure no other instance of the server is running")
            print("Try running 'taskkill /F /IM python.exe' to clear all Python processes")
            sys.exit(1)

# Create the server socket
sock = create_server_socket()

clients = {}
addresses = {}
running = True


def broadcast(msg, prefix=""):
    """Send a message to all connected clients"""
    for connection in clients:
        try:
            connection.send(prefix.encode() + msg)
        except:
            remove_client(connection)


def remove_client(connection):
    """Remove a client and clean up their connection"""
    if connection in clients:
        name = clients[connection]
        del clients[connection]
        if connection in addresses:
            del addresses[connection]
        try:
            connection.close()
        except:
            pass
        broadcast("{} has left the chat".format(name).encode())


def handle_client(connection):
    """Handle individual client connections"""
    try:
        name = connection.recv(1024).decode()
        welcome = "Welcome {}! If you ever want to quit, type quit to exit.".format(name)
        connection.send(welcome.encode())
        msg = "{} has joined the chat".format(name)
        broadcast(msg.encode())
        clients[connection] = name
        
        while running:
            try:
                msg = connection.recv(1024)
                if msg and msg != "quit".encode():
                    broadcast(msg, name + ": ")
                else:
                    connection.send("quit".encode())
                    remove_client(connection)
                    break
            except:
                remove_client(connection)
                break
    except:
        remove_client(connection)


def accept_incoming_connections():
    """Handle incoming connections"""
    while running:
        try:
            connection, address = sock.accept()
            print("{} has connected".format(address))
            connection.send("Welcome to the chatroom".encode())
            addresses[connection] = address
            Thread(target=handle_client, args=(connection,), daemon=True).start()
        except socket.error:
            break


def shutdown_server():
    """Shutdown the server gracefully"""
    global running
    running = False
    # Notify all clients
    for connection in list(clients.keys()):
        try:
            connection.send("Server is shutting down...".encode())
            connection.send("quit".encode())
            connection.close()
        except:
            pass
    # Clear client lists
    clients.clear()
    addresses.clear()
    # Close server socket
    try:
        sock.shutdown(socket.SHUT_RDWR)
        sock.close()
    except:
        pass


if __name__ == '__main__':
    try:
        sock.listen(5)
        print("Server listening on port {}".format(port))
        print("Press Ctrl+C to shutdown the server")
        
        accept_thread = Thread(target=accept_incoming_connections, daemon=True)
        accept_thread.start()
        
        # Keep the main thread running
        accept_thread.join()
        
    except KeyboardInterrupt:
        print("\nShutting down server...")
        shutdown_server()
        sys.exit(0)
    except Exception as e:
        print(f"\nError: {e}")
        shutdown_server()
        sys.exit(1)
