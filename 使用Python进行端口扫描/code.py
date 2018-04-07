# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 12:10:55 2018

@author: peter
"""

import socket


def Get_ip(domain):
    try:
        return socket.gethostbyname(domain)
    except Exception as e:
        print('%s: %s' % (domain, e))
        exit()


def PortScan(ip):
    print("it will take a long time")
    result_list = []
    port_list = range(1, 65535)
    for port in port_list:
        try:
            s = socket.socket()
            s.settimeout(0.1)
            s.connect((ip, port))
            openstr = "PORT:"+str(port) + " OPEN "
            print(openstr)
            result_list.append(port)
            s.close()
        except:
            pass
    print(result_list)


def main():
    domain = input("PLEASE INPUT YOUR TARGET:")
    ip = Get_ip(domain)
    print('IP:'+ip)
    PortScan(ip)


if __name__ == '__main__':
    main()
