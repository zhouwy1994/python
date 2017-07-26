#!/usr/bin/python3

def func (b):
	b = 10;

def func1 (b):
	b[0] = 10;
	print (b)

b = 2
func (b)

print (b)

#b = [2, 4, 6, 8]
#func1 (b)
#print (b)

func1 (b = [1, 2, 4])
print (b)

def func2 (name, age = 20):
	print ("name:", name)
	print ("age:", age)

func2 ("zhouwy")

def func3 (argc, *args):
	print (argc)
	print (args)
func3 ("sADSSA", "ds", 3, 4, 6)
