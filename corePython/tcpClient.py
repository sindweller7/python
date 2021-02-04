#!/usr/bin/env python
from socket import *
from time import ctime

host = '192.168.0.113'
port = 8888
bufsiz = 1024
serAddr = (host, port)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(serAddr)

while(True):
    data = input('please enter your message: ')
    if not data:
        break
    tcpCliSock.send(bytes(data,'utf-8'))
    data_rcv = tcpCliSock.recv(bufsiz)
    if not data_rcv:
        break
    print(data_rcv.decode('utf-8'))