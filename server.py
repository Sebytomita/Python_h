import socket

SER_ADDR = input("Type the server IP address: ")
SER_PORT = int(input("Type the serve port: "))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((SER_ADDR, SER_PORT))
s.listen(1)
print("Server started! Waiting for connections...")
connection, address = s.accept()
print('Client connection with address: ', address)
while 1:
    data = connection.recv(1024)
    if not data: break
    connection.sendall(b'--Message Received --\n')
    print(data.decode('utf-8'))
connection.close()

