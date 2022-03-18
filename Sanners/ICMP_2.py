import socket

from whois import whois

from scapy.all import *
from random import randint


def main():
    ans, uans = sr(IP(dst="10.0.45.220")/ICMP())
    for snd, rcv in ans:
        print(rcv.sprintf("%IP.src% is alive now"))


if __name__ == '__main__':
    main()
