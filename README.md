# Python Chat Room Application 🗨️

[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A modern, real-time chat room application built with Python's socket programming and Tkinter GUI. This application enables multiple clients to connect to a central server and exchange messages in a group chat environment.

![Chat Room Demo](screenshots/demo.png)

## ✨ Features

### Core Features

- Real-time group chat functionality with multi-client support
- Modern Graphical User Interface (GUI) built with Tkinter
- User name input dialog on startup with validation
- Graceful client disconnection handling
- Server broadcast messaging system

### GUI Features

- Clean and intuitive chat window interface
- Dedicated Quit button with confirmation dialog
- Scrollable message history with automatic scrolling
- Full-width message input field with Enter key support
- Dynamic window title showing current user's name
- Proper window closing handling with cleanup
- Error handling with user-friendly message boxes
- Resizable window support for better UX

## 🚀 Quick Start

### Prerequisites

- Python 3.6 or higher
- No external dependencies required! (Uses Python standard library)

### Installation

1. Clone the repository:

```bash
git clone https://github.com/shabbirshuvo/chat_room_application.git
cd chat_room_application
```

2. (Optional) Create and activate a virtual environment:

```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

## 🎮 Usage

### Option 1: Quick Demo

Run the demo script to automatically start a server and two clients with random names:

```bash
python run_demo.py
```

This will:

- Start the chat server
- Launch two chat clients with unique random names
- Open GUI windows for both clients
- Enable chat between the clients
- Clean up processes on Ctrl+C

### Option 2: Manual Setup

1. Start the server:

```bash
python chatroom_server.py
```

2. In separate terminal windows, start multiple clients:

```bash
python chatroom_client.py
```

3. For each client:
   - Enter your name when prompted
   - Start chatting in the GUI window
   - Use the Quit button or close window to exit

## 🔧 How It Works

The application uses Python's socket programming to create a TCP/IP server that handles multiple client connections:

- Server runs on localhost (127.0.0.1) by default
- Uses port 4000 for communication
- Handles multiple simultaneous client connections using threads
- Broadcasts messages to all connected clients
- Implements proper cleanup on client disconnection

## �� Project Structure

```
chat_room_application/
├── chatroom_server.py  # Server implementation
├── chatroom_client.py  # Client implementation with GUI
├── run_demo.py        # Demo script for quick testing
├── requirements.txt   # Project dependencies (none required)
├── LICENSE           # MIT License
└── README.md        # Project documentation
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Create a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Shabbir Shuvo**

- GitHub: [@shabbirshuvo](https://github.com/shabbirshuvo)

## 🌟 Show your support

Give a ⭐️ if this project helped you!
