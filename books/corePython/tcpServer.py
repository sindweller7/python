#!/usr/bin/env python

from socket import *
from time import ctime

host = "192.168.0.106"
port = 8888
bufsiz = 1024
addr = (host,port)

tcpSerSock = socket(AF_INET, SOCK_STREAM)

tcpSerSock.bind(addr)
tcpSerSock.listen(5)

while True:
    print("waiting for connection...")
    tcpCliSock, cliaddr = tcpSerSock.accept()
    print('...connected from:', addr)

    while True:
        data = tcpCliSock.recv(bufsiz)
        if not data:
            break

        resp_message = '[' + ctime() + '] '+ data.decode('utf-8')

        tcpCliSock.send(bytes(resp_message,'utf-8'))

    tcpCliSock.close()

tcpSerSock.close()
