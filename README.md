# Banner Grabber v2

A simple Python-based Banner Grabber that connects to a target server using raw sockets, sends an HTTP GET request, extracts the HTTP response headers, and displays them in a clean, formatted output.

This project was built to strengthen my understanding of:

- TCP Socket Programming
- HTTP Request/Response Structure
- HTTP Header Parsing
- Python Dictionaries
- Network Reconnaissance

---

## Features

- Connects to a target using TCP sockets
- Sends a manual HTTP GET request
- Parses the HTTP response
- Extracts all HTTP response headers
- Displays a clean and formatted output
- Shows:
  - Target
  - IP Address
  - Port
  - HTTP Status
  - Response Headers
  - Summary (Server, Content-Type, Status)
- Handles connection failures gracefully

---

## Project Structure

```
Banner-Grabber/
│
├── grabber.py
└── README.md
└──screenshots
   └──demo.png
```

---

## Requirements

- Python 3.x

No external libraries are required.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/Banner-Grabber.git
```

Move into the project directory:

```bash
cd Banner-Grabber
```

---

## Usage

Run the script:

```bash
python3 grabber.py
```

Example:

```text
Enter target: example.com
Enter Port number to use (http(80) or https(443)): 80
```

---

## Example Output

```text
========================================
            Banner Grabber v2
========================================

Target      : example.com
IP Address  : 104.20.23.154
Port        : 80

========================================
HTTP Status
========================================

HTTP/1.1 200 OK

========================================
Response Headers
========================================

Server              : cloudflare
Content-Type        : text/html
Connection          : close
Transfer-Encoding   : chunked
Date                : Sat, 01 Aug 2026 16:37 GMT

========================================
Summary
========================================

Server       : cloudflare
Content-Type : text/html
Status       : HTTP/1.1 200 OK

Program Completed!!
```

---

## Concepts Practiced

- Socket Programming
- TCP Connections
- HTTP Protocol
- HTTP GET Requests
- HTTP Response Parsing
- Dictionaries
- String Manipulation
- Error Handling

---

## Disclaimer

This tool is intended for educational purposes and should only be used on systems you own or have permission to test.

---
