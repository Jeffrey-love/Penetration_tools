import socket

from whois import whois

from scapy.all import *
from random import randint
import time


def main():
    # ans, uans = sr(IP(dst="10.0.45.220")/TCP(dport=80, flags="S"))
    # for snd, rcv in ans:
    #     print(rcv.sprintf("%IP.src% 80 is up"))
    ip = "192.168.153.135"
    dport = randint(1, 65535)
    packet = IP(dst=ip)/TCP(flags="A", dport=dport)
    response = sr1(packet, timeout=1.0, verbose=0)
    if response:
        # RST
        if int(response[TCP].flags) == 4:
            time.sleep(0.5)
            print(ip+' is up')
        else:
            print(ip+' is down')
    else:
        print('no result')


if __name__ == '__main__':
    main()
