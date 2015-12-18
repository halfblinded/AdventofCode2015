#!/bin/python

ns = 0

with open("input") as f:
	while True:
		i = f.read(1)
		if not i:
			break
		for line in f:
			if line.count('a') + line.count('e') + line.count('i') + line.count('o') + line.count('u') < 3:
				continue
			if 'ab' in line or 'cd' in line or 'pq' in line or 'xy' in line:
				continue
			for c in range(0, len(line)-1):
				if line[c] == line[c+1]:
					ns += 1
					break
print ns
