#! /usr/bin/python
# -*- coding:utf-8 -*-
from scapy.all import *
from whois import whois
import socket
import os
import time
import sys
import whois


# ip查询
def ip_check(url):
    ip = socket.gethostbyname(url)
    print("\n" + url)
    print('ip地址' + ip + "\n")
    print('------------------------------------++++++--------------------------------------')


# whois查询
def whois_check(url):
    data = whois.whois(url)
    print(data)
    print('------------------------------------++++++--------------------------------------')


# CDN判断-利用返回IP条数进行判断
def cdn_check(url):
    print('判断CDN：')
    ns = "nslookup " + url
    # data=os.system(ns)
    # print(data) #结果无法读取操作
    data = os.popen(ns, "r").read()
    print(data)
    if data.count("Address:") > 2:
        print("存在CDN")
    else:
        print("不存在CDN")
    print('------------------------------------++++++--------------------------------------')


# 子域名查询-
# 利用字典记载爆破进行查询
def zym_list_check(url):
    print("子域名爆破中，请等待")
    url = url.replace("www.", "")
    for zym_list in open("../../dnslist.txt"):
        zym_list = zym_list.replace("\n", "")
        zym_list_url = zym_list + "." + url
        try:
            ip = socket.gethostbyname(zym_list_url)
            print("\n" + zym_list_url + "->" + ip + "\n")
            time.sleep(0.1)
        except Exception as e:
            print('.', end="")
            time.sleep(0.1)
    print('\n------------------------------------++++++--------------------------------------')


# 端口扫描
def port_check(url):
    ip = socket.gethostbyname(url)
    # ports = {'21', '22', '135', '443', '445', '80', '1433', '3306', "3389", '1521',
    #          '8000', '7002', '7001', '8080', "9090", '8089', '4848'}
    ports = {'80'}
    # flag = 0
    # for dport in ports:
    #     dport = int(dport)
    #     packet = IP(dst=ip) / TCP(flags="A", dport=dport)
    #     response = sr1(packet, timeout=1.0, verbose=0)
    #     if response:
    #         print(response)
    #         # RST
    #         if int(response[TCP].flags) == 4:
    #             flag = 1
    #             print(ip + ':' + str(dport) + ' is up')
    #         else:
    #             print(ip + ':' + str(dport) + ' is down')
    # if not flag:
    #     print('无法查询到开放端口')
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    for port in ports:

        try:
            data = server.connect((ip, int(port)))
            if data == 0:
                server.shutdown(socket.SHUT_RDWR)
                print(ip + ":" + port + "|open")
            else:
                server.shutdown(socket.SHUT_RDWR)
                print(ip + ":" + port + "|close")
                pass
        except Exception as err:
            print(err)
            pass
    print('------------------------------------++++++--------------------------------------')


# 系统判断
# 1.基于TTL值进行判断
# 2.基于第三方脚本进行判断
def os_check(url):
    data = os.popen("nmap -O " + url, "r").read()
    print(data)
    print('------------------------------------++++++--------------------------------------')


if __name__ == '__main__':
    url = sys.argv[1]
    check = sys.argv[2]
    # print(url +"\n"+ check)
    if check == "all":
        ip_check(url)
        whois_check(url)
        cdn_check(url)
        zym_list_check(url)
        port_check(url)
        os_check(url)
    elif check == "ip":
        ip_check(url)
    elif check == "whois":
        whois_check(url)
    elif check == "cdn":
        cdn_check(url)
    elif check == "zym":
        zym_list_check(url)
    elif check == "port":
        port_check(url)
    elif check == "os":
        os_check(url)