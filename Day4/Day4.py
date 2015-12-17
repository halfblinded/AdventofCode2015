#!/bin/python

import hashlib

counter = 0

while True:
	input = 'yzbqklnj'+str(counter)
	hash = hashlib.md5(input.encode())
	answer = (hash.hexdigest())
	test = answer[0:6]
	counter+=1
	if test == '000000':
		print input, answer
		break

