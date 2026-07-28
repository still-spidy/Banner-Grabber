# Banner Grabber

A simple Python-based Banner Grabber that connects to a web server using raw TCP sockets, sends an HTTP GET request, and extracts the server banner from the HTTP response.

## Features

- Resolve domain names to IP addresses
- Establish TCP connection using sockets
- Send a raw HTTP GET request
- Receive HTTP response
- Extract and display the `Server` header (banner)
- Handles invalid hostnames
- Detects connection failures
- Option to display the complete HTTP response if no banner is found

## Technologies Used

- Python 3
- Socket Programming
- HTTP Protocol

## How It Works

1. User enters a hostname.
2. The program resolves the hostname to an IP address.
3. A TCP connection is established on port **80**.
4. A raw HTTP GET request is sent.
5. The HTTP response is received.
6. The program searches for the **Server** header and displays it.

## Example

```text
Enter target: example.com

Connecting to example.com...
Connection Successful!!

Banner:
Server: cloudflare

Program Completed!!
```

## Project Structure

```
Banner-Grabber/
│
├── banner_grabber.py
├── README.md
└── screenshots/
    └── demo.png
```

## What I Learned

- Socket Programming
- TCP Connections
- DNS Resolution
- HTTP Request & Response Structure
- HTTP Headers
- Banner Grabbing
- Protocol Debugging
- Parsing Server Responses

## Disclaimer

This project is intended for educational purposes only. Use it only on systems that you own or have permission to test.
