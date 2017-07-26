#!/usr/bin/python3

import time

while True:
	try:
		string = int(input())
		print ("Hello Error")
		time.sleep(1)
	except ValueError:
		print ("Oops!  That was no valid number.  Try again   ")
	else:
		raise ValueError
