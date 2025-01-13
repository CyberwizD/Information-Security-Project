#!/usr/bin/python3

import socket

def banner(ip_addr, port):
    s = socket.socket()
    s.connect((ip_addr, int(port)))

    try:
        print(str(s.recv(1024)).strip('b'))

    except ConnectionRefusedError as error:
        print("No connection could be made because the target machine actively refused it.")

if __name__ == "__main__":
    ip_addr = input("Enter an IP address: ")
    port = str(input("Specify the port: "))

    banner(ip_addr, port)
