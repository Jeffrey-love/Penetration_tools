import socket

from whois import whois

from scapy.all import *
from random import randint
import time


def main():
    ip = '10.0.45.220'
    port = 3306
    packet = IP(dst=ip)/TCP(sport=12345, dport=port, flags="S")
    resp = sr1(packet, timeout=20)
    if(str(type(resp)) == '<type "NoneType">'):
        print("port %s is closed" %(port))
    elif(resp.haslayer(TCP)):
        # 判断是否有ACK值
        if(resp.getlayer(TCP).flags == 0x12):
            send_rst = sr(IP(dst=ip)/TCP(sport=12345, dport=80, flags="R"), timeout=20)
            print("port %s is open" %(port))
        # 判断是否拒绝连接
        elif(resp.getlayer(TCP).flags == 0x14):
            print("prot %s is down" %(port))


if __name__ == '__main__':
    main()
