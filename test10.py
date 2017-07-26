#!/usr/bin/python3

fp = open ("./test.txt", "w")

i = 1
while i < 100:
	fp.write ("Hello ,This is from Python\n")
	i += 1
fp.close

fp = open ("./test.txt", "r")

while True:
	str1 = fp.readline()
	print (str1)
	if str1 == "":
		print ("file alawle end!!!")
		break


