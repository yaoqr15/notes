import socket 
import os
import sys

FILE_NAME = "stdfile"

def sendFile(addr, port, filename):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((addr, port))

    fileSize = os.path.getsize(filename)
    client.send(('file %d' % fileSize).encode())

    if client.recv(2).decode() != 'ok':
        return
    with open(filename, 'rb') as f:
        for line in f:
            client.sendall(line)    
    client.close()

def createFile(filename, size):
    os.system("truncate %s -s %s" % (filename, size))

if __name__ == '__main__':
    if len(sys.argv) != 4:
        sys.exit("usage: python socket_client.py [IP_ADDR] [PORT] [SIZE]")
    createFile(FILE_NAME, sys.argv[3])
    sendFile(sys.argv[1], int(sys.argv[2]), FILE_NAME)