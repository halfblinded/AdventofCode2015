#!/bin/python

with open('input', 'r') as f:
	count = 0
	counter = 0
	while True:
		c = f.read(1)
		if not c:
			print "End of File"
			break
		if c == '(':
			count += 1
			counter += 1
		else:
			count -= 1
			counter += 1
		print count,':',counter
