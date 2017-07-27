#!/usr/bin/python3
tmp = 2

var = range(int(input()))
print(var)
for i in [1, 3, 5, 7, 9]:
	while i % tmp != 0:
		tmp += 1
	if tmp == i:
		print (i)
	tmp = 2
