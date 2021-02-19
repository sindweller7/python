import sys
import socket
import getopt
import threading
import subprocess

# define some global variables
listen = False
command = False
upload = False
execute = ""
target = ""
upload_destination = ""
port = 0


def run_command(command):
    command = command.rstrip()
    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
        subprocess.check_output()
    except:
        output = "Fail to exceute command. \r\n"

    return output


def client_handler(client_socket):
    global upload
    global execute
    global command

    if len(upload_destination):
        file_buffer = ""

        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            else:
                file_buffer += data

        try:
            file_descriptor = open(upload_destination, "wb")
            file_descriptor.write(file_buffer)
            file_descriptor.close()

            client_socket.send("Successfully saved file to %s\r\n" % upload_destination)
        except:
            client_socket.send("Failed to save file to %s\r\n" % upload_destination)

    if len(execute):
        output = run_command(execute)
        client_socket.send(output)

    if command:
        while True:
            client_socket.send("<BHP:#> ")
            cmd_buffer = ""
            while "\n" not in cmd_buffer:
                cmd_buffer += client_socket.recv(1024)
                response = run_command(cmd_buffer)

                client_socket.send(response)


def server_loop():
    global target

    if not len(target):
        target = '0.0.0.0'

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((target, port))
    server_socket.listen(5)

    while True:
        client_socket, addr = server_socket.accept()

        clent_thread = threading.Thread(target=client_handler, args=(client_socket,))
        clent_thread.start()


def client_sender(buffer1):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((target, port))

        if len(buffer1):
            client_socket.send(buffer1)

        while True:
            recv_len = 1
            response = ''
            while recv_len:
                data = client_socket.recv(4096)
                recv_len = len(data)
                response += data

                if recv_len < 4096:
                    break
            print response

            buffer1 = raw_input("please enter command")
            buffer1 += '\n'

            client_socket.send(buffer1)

    except:
        print "[*] Exception! Exiting."
        client_socket.close()


def usage():
    print "Netcat Replacement"
    print
    print "Usage: bhpnet.py -t target_host -p port"
    print "-l --listen                - listen on [host]:[port] for incoming connections"
    print "-e --execute=file_to_run   - execute the given file upon receiving a connection"
    print "-c --command               - initialize a command shell"
    print "-u --upload=destination    - upon receiving connection upload a file and write to [destination]"
    print
    print
    print "Examples: "
    print "bhpnet.py -t 192.168.0.1 -p 5555 -l -c"
    print "bhpnet.py -t 192.168.0.1 -p 5555 -l -u=c:\\target.exe"
    print "bhpnet.py -t 192.168.0.1 -p 5555 -l -e=\"cat /etc/passwd\""
    print "echo 'ABCDEFGHI' | ./bhpnet.py -t 192.168.11.12 -p 135"
    sys.exit(0)


def main():
    global listen
    global port
    global execute
    global command
    global upload_destination
    global target

    if not len(sys.argv[1:]):
        usage()

    try:
        opts, remain_args = getopt.getopt(sys.argv[1], 'hle:t:p:cu:', \
                                          ['help', 'listen', 'execute', 'target', 'port', 'command' 'upload'])
    except getopt.GetoptError as err:
        print("error message: ", err)
        usage()

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            usage()
        elif opt in ('-l', '--listen'):
            listen = True
        elif opt in ('-e', '--execute'):
            execute = arg
        elif opt in ('-c', '--commandshell'):
            command = True
        elif opt in ('-u', '--upload'):
            upload_destination = arg
        elif opt in ("-t", "--target"):
            target = arg
        elif opt in ("-p", "--port"):
            port = int(arg)
        else:
            assert False, "Unhandled Option"

        if not listen and len(target) and port > 0:
            buffer = sys.stdin.read()
            client_sender(buffer)
        if listen:
            server_loop()


main()
