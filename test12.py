#!/usr/bin/python3

class Myclass:
	
	def __init__(self, arg1, arg2):
		self.var = arg1
		self.var1 = arg2
	def func(selfd):
		selfd.vare = 122
obj = Myclass(23, 34)


class Myclass1:
	age = ''
	name = ''
	
	__width = 0
	
	def info(self, a, n, w):
		self.age = a
		self.name = n
		self.__width = w
	def pri(self):
		print(self.age)
		print(self.name)
		print(self.__width)

ji = Myclass1()

ji.info(23, "zhouwy", 176)
ji.pri()

