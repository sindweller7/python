from socket import *
from time import ctime

host = '192.168.0.106'
port = 8886
addr = (host, port)
bufsiz = 1024

udp_ser_sock = socket(AF_INET, SOCK_DGRAM)
udp_ser_sock.bind(addr)

while True:
    print('waiting for message...')
    print('-----------------', udp_ser_sock.recvfrom(bufsiz), '--------------------------')
    data, cli_addr = udp_ser_sock.recvfrom(bufsiz)
    message = host + ctime() + data.decode('utf-8')
    udp_ser_sock.sendto(bytes(message, 'utf-8'),cli_addr)
    print('received from and returned to:', cli_addr)

udp_ser_sock.close()

