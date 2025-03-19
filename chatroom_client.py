import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, messagebox, simpledialog

class ChatClient:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = '127.0.0.1'
        self.port = 4000
        self.name = None
        
    def setup_gui(self):
        # Main window setup
        self.window = tk.Tk()
        self.window.title(f"Chat Room - {self.name}")
        self.window.geometry("600x450")
        self.window.resizable(True, True)
        
        # Create main frame
        main_frame = tk.Frame(self.window)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # Chat display area
        self.chat_area = scrolledtext.ScrolledText(main_frame, wrap=tk.WORD, height=20)
        self.chat_area.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Bottom frame for input and buttons
        bottom_frame = tk.Frame(main_frame)
        bottom_frame.pack(fill=tk.X, padx=5, pady=5)
        
        # Message entry
        self.msg_entry = tk.Entry(bottom_frame)
        self.msg_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        self.msg_entry.bind('<Return>', lambda e: self.send_message())
        
        # Button frame
        button_frame = tk.Frame(bottom_frame)
        button_frame.pack(side=tk.RIGHT)
        
        # Send button
        self.send_button = tk.Button(button_frame, text="Send", command=self.send_message)
        self.send_button.pack(side=tk.LEFT, padx=5)
        
        # Quit button
        self.quit_button = tk.Button(button_frame, text="Quit", command=self.on_closing, bg='#ff9999')
        self.quit_button.pack(side=tk.LEFT, padx=5)
        
        # Window close handler
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        # Disable input until connected
        self.msg_entry.config(state='disabled')
        self.send_button.config(state='disabled')
        
    def get_username(self):
        while True:
            name = simpledialog.askstring("Name Input", "Enter your name:", parent=self.window)
            if name:
                if len(name.strip()) > 0:
                    return name.strip()
            else:
                if messagebox.askokcancel("Quit", "Do you want to quit?"):
                    self.window.destroy()
                    return None
                
    def connect(self):
        try:
            # Setup GUI first
            self.setup_gui()
            
            # Connect to server
            self.sock.connect((self.host, self.port))
            welcome = self.sock.recv(1024).decode()
            
            # Get username through dialog
            self.name = self.get_username()
            if not self.name:
                return
                
            # Update window title with username
            self.window.title(f"Chat Room - {self.name}")
            
            # Send username to server
            self.sock.send(self.name.encode())
            
            # Enable input
            self.msg_entry.config(state='normal')
            self.send_button.config(state='normal')
            self.msg_entry.focus()
            
            # Display welcome message
            self.chat_area.insert(tk.END, welcome + '\n')
            
            # Start receiving thread
            receive_thread = threading.Thread(target=self.receive_messages)
            receive_thread.daemon = True
            receive_thread.start()
            
            self.window.mainloop()
            
        except Exception as e:
            messagebox.showerror("Error", f"Could not connect to server: {str(e)}")
            self.window.destroy()
    
    def receive_messages(self):
        while True:
            try:
                message = self.sock.recv(1024).decode()
                if message == "quit":
                    break
                self.chat_area.insert(tk.END, message + '\n')
                self.chat_area.see(tk.END)
            except:
                break
    
    def send_message(self):
        message = self.msg_entry.get().strip()
        if message:
            if message.lower() == "quit":
                self.on_closing()
            else:
                self.sock.send(message.encode())
                self.msg_entry.delete(0, tk.END)
    
    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            try:
                self.sock.send("quit".encode())
            except:
                pass
            self.window.destroy()
            self.sock.close()

if __name__ == "__main__":
    client = ChatClient()
    client.connect()
