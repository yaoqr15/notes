import socket
import sys 
import os

FILE_NAME = "newfile"

def receiveFile(addr, port, filename):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((addr, port))
    server.listen(5)
    conn, clientAddr = server.accept()

    tmp = conn.recv(32).decode()
    fileSize = int(tmp.split()[1])
    if fileSize != 0:
        conn.send('ok'.encode())
    else:
        return
    if os.path.exists(filename):
        os.remove(filename)
    with open(filename, 'wb') as f:
        recvSize = 0
        while recvSize < fileSize:
            line = conn.recv(8192)
            f.write(line)
            recvSize += len(line)
        conn.close()
    server.close()

if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.exit("usage: python socket_server.py [IP_ADDR] [PORT]")
    receiveFile(sys.argv[1], int(sys.argv[2]), FILE_NAME)