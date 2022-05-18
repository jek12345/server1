import time, socket, sys

new_socket = socket.socket()
new_socket.bind(("212.76.128.141", 2000))
print( "Binding successful!")
print("This is your IP: ", "212.76.128.141")
name = input('Enter name: ')
new_socket.listen(1)
conn, add = new_socket.accept()
print("Received connection from ", add[0])
print('Connection Established. Connected From: ',add[0])
client = (conn.recv(1024)).decode()
print(client + ' has connected.')
conn.send(name.encode())
while True:
    message = conn.recv(1024)
    message = message.decode()
    print(client, ':', message)
