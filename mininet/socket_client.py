import socket
from datetime import datetime

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
print(host)
port = 9999
s.connect((host, port))

start = datetime.now()
while True:
    msg = s.recv(1024)
    if msg.decode() == 'exit':
        end = datetime.now()
        print("Finish in %f seconds" % (end - start).total_seconds())
        break
s.close()