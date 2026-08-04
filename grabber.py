import socket
import json

def banner_grabber(target):
    try: 
        ip = socket.gethostbyname(target)
    except:
        print("Invalid Hostname or IP Address")
        exit()
    port = (80)
    print(f"Connecting to {target}....")
    request = ("GET / HTTP/1.1\r\n"
    f"Host: {target}\r\n"
    "Connection: close\r\n"
    "\r\n")

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(10)
    status = s.connect_ex((ip,port))
    if status!=0:
        print("Connection Failed! \n Exiting Program.....bye")
        exit()
    else:
        print("Connection Successfull!!")
    s.sendall(request.encode())
    result = s.recv(1024)
    s.close()
    result_decode = result.decode()

    #Converting whole string into dictionary of headers and values
    data = []
    for line in result_decode.split("\r\n\r\n"):
        data = line.splitlines()
        break

    new_data = {}
    for words in data[1::]:
        key, value = words.split(":",1)
        new_data[key.strip()] = value.strip()

    print("========================================\r\n"
            "       Banner Grabber v2\r\n"
    "========================================\r\n\r\n"

    f"Target      : {target}\r\n"
    f"IP Address  : {ip}\r\n"
    f"Port        : {port}\r\n\r\n"

    "========================================\r\n"
    "           HTTP Status\r\n"
    "========================================\r\n\r\n"

    f"{data[0]}\r\n\r\n"

    "========================================\r\n"
    "            Response Headers\r\n"
    "========================================\r\n")

    for key, value in new_data.items():
        print(f"{key:<20}:{value}")

    print("\r\n")
    print("========================================\r\n"
    "             Summary\r\n"
    "========================================\r\n\r\n"

    f"Server      : {new_data.get("Server","Not Disclosed")}\r\n"
    f"ContentType : {new_data.get("Content-Type","Unknown")}\r\n"
    f"Status      : {data[0]}\r\n")



    print("Program Completed!!")

hostname = input("Enter target: ")
banner_grabber(hostname)