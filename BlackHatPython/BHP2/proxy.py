#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import sys
import socket
import threading


# 仿wireshark函数,输出1、数据序号 2、十六进制数据 3、可以正常显示的asci字符
def hexdump(src, length=16, show=True):
    if isinstance(src, bytes):
        src = src.decode()

    results = list()
    for i in range(0, len(src), length):
        word = str(src[i: i + length])
        printable = ''.join([x if 0x20 <= ord(x) < 0x7f else '.' for x in word])
        hexa = " ".join(f"{ord(c):04X}" for c in word)
        hexwidth = length * 3
        # i:04x(取出i的值,用4位16进制数显示,不足4位的补0) < (左对齐)
        results.append(f"{i:04X}    {hexa:<{hexwidth}}    {printable}")
    if show:
        for line in results:
            print(line)
        else:
            return results


def receive_from(sock_conn):
    buffer = b""
    sock_conn.settimeout(5)
    try:
        while True:
            data = sock_conn.recv(4096)
            if not data:
                break
            buffer += data
    except Exception as e:
        print("error: ", e)
    return buffer


def request_handler(buffer):
    # perform packet modifications
    return buffer


def response_handler(buffer):
    # perform packet modifications
    return buffer


def proxy_handler(client_socket, remote_host, remote_port, receive_first):
    remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    remote_socket.connect((remote_host, remote_port))

    if receive_first:
        remote_buffer = receive_from(remote_socket)
        hexdump(remote_buffer)

        remote_buffer = response_handler(remote_buffer)
        if len(remote_buffer):
            print("[<==] sending %d bytes to localhost." % len(remote_buffer))
            client_socket.send(remote_buffer)

    while True:
        local_buffer = receive_from(client_socket)
        if len(local_buffer):
            line = "[==>] 收到 %d bytes 从本地客户端发来的数据. " % len(local_buffer)
            print(line)
            hexdump(local_buffer)

            local_buffer = request_handler(local_buffer)
            remote_socket.send(local_buffer)
            print("[==>] 代理将数据发给远端.")

        remote_buffer = receive_from(remote_socket)
        if len(remote_buffer):
            print("[<==] 从远端收到 %d bytes 数据. " % len(remote_buffer))
            hexdump(remote_buffer)

            remote_buffer = response_handler(remote_buffer)
            client_socket.send(remote_buffer)
            print("[<==] 代理发送远端数据给本地客户端.")

        if not len(local_buffer) or not len(remote_buffer):
            client_socket.close()
            remote_socket.close()
            print("[*] 未收到更多数据,关闭连接.")


def server_loop(local_host, local_port, remote_host, remote_port, receive_first):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.bind((local_host, local_port))
    except Exception as e:
        print("绑定失败: %r" % e)
        print("[!!] 在 %s:%d 启动监听失败." % (local_host, local_port))
        print("[!!] 处理建议:1、更换监听端口 2、确认是否拥有权限")
        sys.exit(0)

    print("[*] 在 %s:%d 启动监听" % (local_host, local_port))
    server.listen(5)

    while True:
        client_socket, addr = server.accept()
        line = "> 从 %s:%d 收到连接请求" % (addr[0], addr[1])
        print(line)

        # 启动一个线程,和远端主机进行通信
        proxy_thread = threading.Thread(
            target=proxy_handler, args=(client_socket, remote_host, remote_port, receive_first))
        proxy_thread.start()


def main():
    if len(sys.argv[1:]) != 5:
        print("Usage: ./proxy.py [localhost] [localport]", end='')
        print("[remotehost] [remoteport] [receive_first]")
        print("Example: ./proxy.py 127.0.0.1 9000 10.12.132.1 9000 True")
        sys.exit(0)

    local_host = sys.argv[1]
    local_port = int(sys.argv[2])

    remote_host = sys.argv[3]
    remote_port = int(sys.argv[4])

    receive_first = sys.argv[5]

    if "True" in receive_first:
        receive_first = True
    else:
        receive_first = False

    server_loop(local_host, local_port, remote_host, remote_port, receive_first)


if __name__ == "__main__":
    main()
