import socket

from whois import whois

from scapy.all import *
from random import randint
import time


def main():
    ip = '10.0.45.220'
    ans, uans = sr(IP(dst=ip)/UDP(dport=80))
    for snd, rcv in ans:
        print(rcv.sprintf("%IP.src% is up"))


if __name__ == '__main__':
    main()
