#!/usr/bin/python3

class people:
	name = ''
	age = ''
	
	__weight = ''
	
	def __init__(self, n, a, w):
		self.name = n
		self.age = a
		self.__weight = w
	def speak(self):
		print("Hello,I am %s, This year is %d old, My weight is %d" \
		%(self.name, self.age, self.__weight))


class student(people):
	grade = ''
	def __init__(self, n, a, w, g):
		people.__init__(self ,n ,a ,w)
		self.grade = g
	
	def speak(self):
		print("Hello,I am %s, This year is %d old, I am from %d grade" \
		%(self.name, self.age, self.grade))

class speaker:
	topic = ''
	name = ''
	
	def __init__(self, t, n):
		self.topic = t
		self.name = n
	def speak(self):
		print("I am a speaker, My name is %s, speak topic about \"%s\" today" \
		%(self.name, self.topic))

class smaple(speaker, student):
	
	name = ''
	def __init__(self, n, a, w, g, t):
		speaker.__init__(self, t, "wangmin")
		student.__init__(self, "wangyulan", a, w, g)
		name = n

class Vector():
	a = ''
	b = ''
	
	def __init__(self, a, b):
		self.a = a
		self.b = b
	def __str__(self):
		return 'Vector (%d, %d)' % (self.a, self.b)
		
	def __add__(self, other):
		return Vector(self.a + other.a, self.b + other.b)
		
obj1 = Vector(2, 4)
obj2 = Vector(3, -9)

print(obj1 + obj2)















