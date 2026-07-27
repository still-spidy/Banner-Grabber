import socket

hostname = input("Enter target: ")
ip = socket.gethostbyname(hostname)
port = 80
data = ("GET / HTTP/1.1\r\n"
f"Host: {hostname}\r\n"
"Connection: close\r\n"
"\r\n")
print(repr(data))
print(data.encode())


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.settimeout(10)
status = s.connect_ex((ip,port))
print(status)
print(s.sendall(data.encode()))
s.sendall(data.encode())
result = s.recv(1024)
s.close()
result_decode = result.decode()
print(result_decode)
