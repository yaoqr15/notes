import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()

port = 9999
serversocket.bind((host, port))

serversocket.listen(5)


clientsocket, addr = serversocket.accept()
print("连接底座：%s"%str(addr))
# while True:
buffer = ''.zfill(1024000000)
clientsocket.send(buffer.encode())

clientsocket.send('exit'.encode())
clientsocket.close()
