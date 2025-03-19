# Python Chat Room Application 🗨️

[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A modern, real-time chat room application built with Python's socket programming and Tkinter GUI. This application enables multiple clients to connect to a central server and exchange messages in a group chat environment.

## 🖥️ System Requirements

- Any operating system (Windows, macOS, Linux)
- Minimum 512MB RAM
- 50MB free disk space
- Display resolution: 1024x768 or higher

## ✨ Features

### Core Features

- Real-time group chat functionality with multi-client support
- Modern Graphical User Interface (GUI) built with Tkinter
- User name input dialog on startup with validation
- Graceful client disconnection handling
- Server broadcast messaging system
- Graceful server shutdown with client notifications
- Automatic port cleanup and reuse
- Robust error handling and process management

### GUI Features 🎨

- Clean and intuitive chat window interface
- Dedicated Quit button with confirmation dialog
- Scrollable message history with automatic scrolling
- Full-width message input field with Enter key support
- Dynamic window title showing current user's name
- Proper window closing handling with cleanup
- Error handling with user-friendly message boxes
- Resizable window support for better UX

### Process Management 🔄

- Automatic cleanup of zombie processes
- Port availability checking
- Process monitoring and status tracking
- Graceful shutdown of all components
- Comprehensive error handling

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

### Option 1: Quick Demo (Recommended)

Run the demo script to automatically start a server and two clients with random names:

```bash
python run_demo.py
```

This will:

- Start the chat server
- Launch two chat clients with unique random names
- Open GUI windows for both clients
- Enable chat between the clients
- Handle client closures gracefully
- Clean up processes automatically

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

## 🔧 Technical Details

### Server Features

- Runs on localhost (127.0.0.1) by default
- Uses port 4000 for communication
- Handles multiple simultaneous client connections using threads
- Implements automatic socket cleanup and port reuse
- Graceful shutdown with client notifications
- Robust error handling and recovery

### Client Features

- GUI-based interface using Tkinter
- Automatic name validation
- Real-time message updates
- Connection status monitoring
- Graceful disconnection handling
- Error recovery and reconnection attempts

### Process Management 🔄

- Automatic cleanup of zombie processes
- Port availability checking
- Process monitoring and status tracking
- Graceful shutdown of all components
- Comprehensive error handling

## 📁 Project Structure

```
chat_room_application/
├── chatroom_server.py  # Server implementation
├── chatroom_client.py  # Client implementation with GUI
├── run_demo.py        # Demo script for quick testing
├── requirements.txt   # Project dependencies (none required)
├── LICENSE           # MIT License
└── README.md        # Project documentation
```

## 🚫 Common Issues and Solutions

1. Port Already in Use 🔌

   - The application will automatically attempt to clean up and retry
   - If that fails, manually kill Python processes:

     ```bash
     # Windows
     taskkill /F /IM python.exe

     # Linux/Mac
     pkill -f python
     ```

2. Client Connection Issues 🌐

   - Ensure the server is running first
   - Check if the port is not blocked by firewall
   - Try restarting the application

3. Process Cleanup 🧹

   - The demo script handles cleanup automatically
   - For manual cleanup, use the commands above
   - Wait a few seconds between stopping and starting

## ✉️ Contact

For any questions or feedback, feel free to reach out:

- Email: your.email@example.com (optional)
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/yourusername) (optional)

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
