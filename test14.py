#!/usr/bin/python3

import socket
import sys

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 9999
msg = ''
clientsocket.connect((host, port))

while msg != 'zhou':
	msg = input()
	clientsocket.send(msg.encode('utf-8'))

clientsocket.close()


