import socket 

Host = '127.0.0.1'
port = 9999

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'hello, Server')
    data = s.recv(1024)

print('Recieved', repr(data))