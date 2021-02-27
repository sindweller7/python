import socket

host = '192.168.0.106'
port = 8886
bufsiz = 1024
ser_addr = (host,port)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    data = input('enter your message to server: > ')
    if not data:
        break
    client_socket.sendto(bytes(data, 'utf-8'), ser_addr)
    print('-------------------------------',client_socket.recvfrom(bufsiz),'--------------------------')
    ser_data, addr = client_socket.recvfrom(bufsiz)
    if not ser_data:
        break
    print(ser_data.decode('utf-8'))
    print(addr)

client_socket.close()
