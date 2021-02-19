import sys
import socket
import threading

def server_loop():
    pass

def hexdump(src, length=30):
    result = []
    digits = 4 if isinstance(src, unicode) else 2
    print isinstance(src, unicode)

    for i in xrange(0, len(src), length):
        s = src[i:i+length]
        #0补位,*取出后面计算出来的精度.因此是一个取值,两个参数.digits为精度
        hexa = b' '.join(["%0*x"%(digits, ord(x))  for x in s])
        text = b''.join([x if 0x20 <=ord(x) <0x7f else b'.' for x in s])
        result.append(b"%04x    %-*s    %s" %(i, length*(digits + 1), hexa, text))

    print b'\n'.join(result)

def receive_from(connection):
    buffer = ""
    connection.settimeout(2)
    try:
        while True:
            data = connection.recv(4096)
            if not data:
                break
            buffer += data
    except:
        pass
    return buffer

hexdump("你User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36Netcat:python netcat.py -t 0.0.0.0 -p 5555 -l -cpython netcat.py -t 192.168.0.106 -p 5555")