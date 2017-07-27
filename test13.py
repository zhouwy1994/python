#!/usr/bin/python3

import socket
import sys

#create socket of server object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#get hostname
host = socket.gethostname()

#set listen port
port = 9999

#bind the port
serversocket.bind((host, port))

#set listen number
serversocket.listen(5)
msg = ''
while True:
	clientsocket, cliaddr = serversocket.accept()
	# print('client addr:', cliaddr)
	while msg != "zhou":
		msg = clientsocket.recv(1024)
		print(msg.decode('utf-8'))
	# msg = "Hello My name is zhouwy"
	# clientsocket.send(msg.encode('utf-8'))
	print('exit')
	clientsocket.close()
	