import subprocess
import sys
import time
import random
import os
from threading import Thread

def generate_name():
    adjectives = ['Happy', 'Lucky', 'Clever', 'Bright', 'Swift', 'Kind', 'Brave', 'Wise']
    nouns = ['Panda', 'Fox', 'Eagle', 'Dolphin', 'Tiger', 'Wolf', 'Bear', 'Lion']
    return f"{random.choice(adjectives)}{random.choice(nouns)}"

def start_server():
    print("Starting chat server...")
    subprocess.Popen([sys.executable, "chatroom_server.py"])
    time.sleep(2)  # Wait for server to start

def start_client(client_name):
    print(f"Starting client: {client_name}")
    # Create a new Python process for the client
    process = subprocess.Popen([sys.executable, "chatroom_client.py"],
                             stdin=subprocess.PIPE,
                             text=True)
    
    # Send the client name
    process.stdin.write(f"{client_name}\n")
    process.stdin.flush()
    return process

def main():
    # Clear the terminal
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("=== Chat Room Demo ===")
    print("Starting demo with two automated clients...")
    
    # Start the server
    start_server()
    
    # Generate unique names for clients
    client1_name = generate_name()
    client2_name = generate_name()
    while client2_name == client1_name:
        client2_name = generate_name()
    
    # Start two clients
    client1 = start_client(client1_name)
    time.sleep(1)
    client2 = start_client(client2_name)
    
    print("\nDemo is running!")
    print(f"Client 1: {client1_name}")
    print(f"Client 2: {client2_name}")
    print("\nThe chat windows should now be open.")
    print("You can interact with both clients through their respective GUI windows.")
    print("\nPress Ctrl+C to end the demo...")
    
    try:
        # Keep the script running
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nEnding demo...")
        # Cleanup
        client1.terminate()
        client2.terminate()
        # Find and terminate the server process
        if os.name == 'nt':  # Windows
            os.system('taskkill /f /im python.exe /fi "windowtitle eq chatroom_server.py"')
        else:  # Linux/Mac
            os.system("pkill -f chatroom_server.py")

if __name__ == "__main__":
    main() 