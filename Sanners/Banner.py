import socket

from whois import whois

from scapy.all import *
from random import randint
import time


def main():
    ip = '192.168.153.135'
    port = 445

    s = socket.socket()
    s.connect((ip, port))
    s.send('haha'.encode())
    banner = s.recv(1024)
    s.close()
    print("banner is {}".format(banner))


if __name__ == '__main__':
    main()
