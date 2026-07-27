import socket

try: 
    hostname = input("Enter target: ")
    ip = socket.gethostbyname(hostname)
except:
    print("Invalid Hostname or IP Address")
    exit()
port = 80
print(f"Connecting to {hostname}....")
data = ("GET / HTTP/1.1\r\n"
f"Host: {hostname}\r\n"
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
s.sendall(data.encode())
result = s.recv(1024)
s.close()
result_decode = result.decode()

banner_found=False
for line in result_decode.splitlines():
    if line.lower().startswith("server:"):
        print(f"Banner Found:\n{line}")
        banner_found=True

if not banner_found:
    print("No banner Found.")
    response = input("Want to see server response(Y/N)?")
    if response.lower()=="y":
        print(result_decode) 

print("Program Completed!!")