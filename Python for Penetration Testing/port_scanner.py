#!/usr/bin/python3

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)

host = input("Enter an IP address: ")
port = int(input("Specify a port to scan: "))

def portScanner(port):
    if s.connect_ex((host, port)):
        print("Port closed.")

    else:
        print("Port open!")

if __name__ == '__main__':
    portScanner(port)