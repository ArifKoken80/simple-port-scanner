# Simple Port Scanner

Python-based multi-threaded port scanner.

## Features
- Port scanning
- Service detection
- Banner grabbing
- Multi-threading

## Usage
python main.py

## Disclaimer
Educational purposes only.

## 📌 Project Lifecycle

### 1. Idea
This project was developed to understand the fundamentals of TCP port scanning and basic network reconnaissance techniques. The main goal was to build a simple tool that can detect open ports on a target system.

### 2. Planning
Before development, the following features were defined:
- Scan a target IP address
- Support port range scanning (e.g. 1–1000)
- Display open ports clearly
- Keep the tool lightweight and simple

Python was chosen as the programming language due to its simplicity and strong networking libraries.

### 3. Design
The project was structured around Python’s socket library. A simple modular structure was considered to separate scanning logic and input handling.

Basic flow:
- Take user input (IP + port range)
- Iterate through ports
- Try TCP connection using sockets
- Return open ports

### 4. Development
The scanner was implemented using Python’s built-in `socket` module. A loop was used to iterate through the specified port range and attempt connections to each port.

### 5. Testing
The tool was tested on:
- Localhost (127.0.0.1)
- Local network devices

Different port ranges were used to verify accuracy and performance.

### 6. Deployment
The project was published on GitHub as an open-source repository. A README file was added to explain usage and functionality.

### 7. Future Improvements
- Add multithreading for faster scanning
- Add service detection (banner grabbing)
- Export results to file (JSON/TXT)
- Improve CLI arguments (--host, --ports)
