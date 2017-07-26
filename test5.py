#!/usr/bin/python3

a, b = 0, 1

while (b < 1000):
	a, b = b, a+b

age = int(input("please input your dog's age"))

if age < 0:
	print ("fack you")
elif age == 1:
	print ("1")	
elif age == 2:
	print ("2")	
else:
	print ("otenrt")


