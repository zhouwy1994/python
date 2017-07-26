#!/usr/bin/python

import sys, getopt

def main(argv):
	inputfile = ''
	outputfile = ''
	try:
		opts, args = getopt.getopt(argv, "hi:o:", ["help", "inputfile=", "noutputfile="])
	except getopt.GetoptError:
		print("test3.py -i inputfile -o outputfile")
		sys.exit(2)
	for opt, arg in opts:
		if opt in ("-h", "--help"):
			print("usage:test3.py -i inputfile -o outputfile")
			sys.exit()
		elif opt in ("-i", "--inputfile"):
			inputfile = arg
		elif opt in ("-o", "--outputfile"):
			outputfile = arg
	print("inputfile:", inputfile)
	print("outputfile:", outputfile)

if __name__ == "__main__":
	main(sys.argv[1:])
		


