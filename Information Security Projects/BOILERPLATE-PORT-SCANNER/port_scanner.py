import socket
import re
from common_ports import ports_and_services  # This file should contain a dictionary of common ports


def get_open_ports(target, port_range, verbose=False):
    open_ports = []

    # Validate if the target is a valid IP address or hostname
    try:
        ip = socket.gethostbyname(target)
    except socket.gaierror:
        if re.match(r'^(\d{1,3}\.){3}\d{1,3}$', target):  # Check if it's an IP address format
            return "Error: Invalid IP address"
        else:
            return "Error: Invalid hostname"

    # Scanning the ports in the given range
    for port in range(port_range[0], port_range[1] + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # 1 second timeout

        result = sock.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()

    # If verbose mode is true, format the output string
    if verbose:
        # Resolve the hostname if the target is an IP address
        try:
            hostname = socket.gethostbyaddr(ip)[0]
        except socket.herror:
            hostname = target

        output = f"Open ports for {hostname} ({ip})\n"
        output += "PORT     SERVICE\n"

        for port in open_ports:
            service = ports_and_services.get(port, "unknown")  # Fetch service from common_ports.py
            output += f"{str(port).ljust(9)}{service}\n"

        return output.strip()

    return open_ports


# Non-verbose mode
print(get_open_ports("209.216.230.240", [440, 445]))
print(get_open_ports("www.stackoverflow.com", [79, 82]))

# Verbose mode
print(get_open_ports("scanme.nmap.org", [20, 80], True))