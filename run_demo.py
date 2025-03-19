import subprocess
import sys
import time
import random
import os
import socket
from threading import Thread

def generate_name():
    adjectives = ['Happy', 'Lucky', 'Clever', 'Bright', 'Swift', 'Kind', 'Brave', 'Wise']
    nouns = ['Panda', 'Fox', 'Eagle', 'Dolphin', 'Tiger', 'Wolf', 'Bear', 'Lion']
    return f"{random.choice(adjectives)}{random.choice(nouns)}"

def is_port_in_use(port):
    """Check if a port is in use"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.bind(('127.0.0.1', port))
            return False
        except socket.error:
            return True

def kill_python_processes():
    """Kill all Python processes"""
    if os.name == 'nt':  # Windows
        os.system('taskkill /F /IM python.exe')
    else:  # Linux/Mac
        os.system("pkill -f python")
    time.sleep(2)  # Wait for processes to be killed

def wait_for_server(timeout=10):
    """Wait for server to start and verify it's running"""
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect(('127.0.0.1', 4000))
                s.close()
                return True
        except:
            time.sleep(0.5)
    return False

def start_server():
    """Start the chat server"""
    print("Starting chat server...")
    
    # Check if port is in use
    if is_port_in_use(4000):
        print("Port 4000 is already in use. Cleaning up existing processes...")
        kill_python_processes()
        time.sleep(2)  # Give extra time for cleanup
        
        # Check again
        if is_port_in_use(4000):
            print("Failed to free up port 4000. Please manually close any running Python processes.")
            sys.exit(1)
    
    # Start the server
    server_process = subprocess.Popen([sys.executable, "chatroom_server.py"],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE,
                                    universal_newlines=True)
    
    # Wait for server to start
    if not wait_for_server():
        print("Failed to start server. Server output:")
        output, error = server_process.communicate()
        if output:
            print("Output:", output)
        if error:
            print("Error:", error)
        kill_python_processes()
        sys.exit(1)
    
    print("Server started successfully!")
    return server_process

def start_client(client_name):
    """Start a chat client with the given name"""
    print(f"Starting client: {client_name}")
    try:
        process = subprocess.Popen([sys.executable, "chatroom_client.py"],
                                 stdin=subprocess.PIPE,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE,
                                 text=True)
        
        # Send the client name
        process.stdin.write(f"{client_name}\n")
        process.stdin.flush()
        
        # Give the client some time to start
        time.sleep(1)
        
        # Check if process is still running
        if process.poll() is not None:
            print(f"Client {client_name} failed to start. Error:")
            _, error = process.communicate()
            print(error)
            return None
            
        return process
    except Exception as e:
        print(f"Error starting client {client_name}: {e}")
        return None

class ChatDemo:
    def __init__(self):
        self.server_process = None
        self.clients = {}  # name -> process
        self.running = True

    def start(self):
        """Start the chat demo"""
        try:
            # Start server
            self.server_process = start_server()
            
            # Generate unique names for clients
            client1_name = generate_name()
            client2_name = generate_name()
            while client2_name == client1_name:
                client2_name = generate_name()
            
            # Start clients
            client1 = start_client(client1_name)
            if not client1:
                raise Exception("Failed to start first client")
            self.clients[client1_name] = client1
            
            client2 = start_client(client2_name)
            if not client2:
                raise Exception("Failed to start second client")
            self.clients[client2_name] = client2
            
            print("\nDemo is running!")
            print(f"Client 1: {client1_name}")
            print(f"Client 2: {client2_name}")
            print("\nThe chat windows should now be open.")
            print("You can interact with both clients through their respective GUI windows.")
            print("Close a client window or type 'quit' to exit that client.")
            print("\nPress Ctrl+C to end the entire demo...")
            
            # Monitor processes
            while self.running and len(self.clients) > 0:
                time.sleep(1)
                
                # Check server
                if self.server_process.poll() is not None:
                    raise Exception("Server process died unexpectedly")
                
                # Check clients and remove closed ones
                closed_clients = []
                for name, process in self.clients.items():
                    if process.poll() is not None:
                        print(f"\nClient {name} has closed.")
                        closed_clients.append(name)
                
                # Remove closed clients
                for name in closed_clients:
                    del self.clients[name]
                
                if len(self.clients) == 0:
                    print("\nAll clients have closed. Ending demo...")
                    break
                    
        except KeyboardInterrupt:
            print("\nEnding demo...")
        except Exception as e:
            print(f"\nError: {e}")
        finally:
            self.cleanup()

    def cleanup(self):
        """Clean up all processes"""
        print("Cleaning up processes...")
        try:
            # Terminate remaining clients
            for process in self.clients.values():
                try:
                    process.terminate()
                except:
                    pass
            
            # Terminate server
            if self.server_process:
                self.server_process.terminate()
        except:
            pass
        
        # Make sure all Python processes are cleaned up
        kill_python_processes()
        print("Demo ended.")

def main():
    # Clear the terminal
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("=== Chat Room Demo ===")
    print("Starting demo with two automated clients...")
    
    demo = ChatDemo()
    demo.start()

if __name__ == "__main__":
    main() 