#!/usr/bin/python

import _thread
import time

def function_thread(name, num):
	while num != 0:
		time.sleep(1)
		print('I am :', name)
		num -= 1

try:
	_thread.start_new_thread(function_thread, ('thread1', 8))
	_thread.start_new_thread(function_thread, ('thread2', 6))
except:
	print('Start Thread Faild')
	
while True:
	pass
	