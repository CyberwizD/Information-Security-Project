#!/usr/bin/python3

import nmap

scanner = nmap.PortScanner()

print("Usage: python3 nmap_scanner.py")
print("<---------------------------->\n")

ip_addr = input("Enter an IP address to scan: ")

print("IP address: ", ip_addr)

type(ip_addr)

resp = input("""\nEnter the type of scan:
1) SYN ACK Scan
2) UDP Scan
3) Full Scan
\n----------> """)

print(f"Selected option: {resp}")

if resp == '1':
    print("Nmap version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sS')

    print(scanner.scaninfo())
    print("IP stats: ", scanner[ip_addr].state())

    print("IP protocol: ", scanner[ip_addr].all_protocols())  # Returns all the IP protocols
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())  # Returns all the active ports

elif resp == '2':
    print("Nmap version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sU')

    print(scanner.scaninfo)
    print("IP stats: ", scanner[ip_addr].state())
    
    print(scanner[ip_addr].all_protocols())
    print("Open prots: ", scanner[ip_addr]['udp'].keys())

elif resp == '3':
    print("Nmap version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sS -sV -sC -A -O')

    print(scanner.scaninfo())
    print("IP stats: ", scanner[ip_addr].state())

    print(scanner[ip_addr].all_protocols())
    print("Open ports: ", scanner[ip_addr]['tcp'].keys())

else:
    print("Enter a valid option!")