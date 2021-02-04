import time

def loop0(second):
    print("loop0 start at: " + time.ctime())
    time.sleep(second)
    print("loop0 stop at: " + time.ctime())

def loop1(second):
    print("loop1 start at: " + time.ctime())
    time.sleep(second)
    print("loop1 stop at: " + time.ctime())

def main():
    print("main function start at:" + time.ctime())
    loop0(2)
    loop1(4)
    print("main function stop at:" + time.ctime())

if __name__ == '__main__':
    main()