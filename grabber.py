import socket

hostname = input("Enter target: ")
ip = socket.gethostbyname(hostname)
port = 80
print(f"Connecting to {hostname}....")
data = ("GET / HTTP/1.1\r\n"
f"Host: {hostname}\r\n"
"Connection: close\r\n"
"\r\n")

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.settimeout(10)
status = s.connect_ex((ip,port))
if status==0:
    print("Connection Successfull!!")
else:
    print("Connection Failed!!")
s.sendall(data.encode())
result = s.recv(1024)
s.close()
result_decode = result.decode()

for line in result_decode.splitlines():
    if line.lower().startswith("server:"):
        print(f"Banner is {line}")

print("Program Completed!!")