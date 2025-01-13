#!/usr/bin/python3

import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 444

server_socket.bind((host, port))

server_socket.listen(3)

while True:
    client_socket, address = server_socket.accept()

    print("Received connection from %s" % str(address))

    message = "Connecting to the server..." + "\r\n" + "Connected."

    client_socket.send(message.encode('ascii'))

    client_socket.close()