#!/usr/bin/env python3

import sys
list_1 = [1, 2, 3, 4, 6]

tr = iter(list_1)
next(tr)
while True:
	try:
		print (next(tr))
	except StopIteration:
		sys.exit()


