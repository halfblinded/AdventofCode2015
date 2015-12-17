#!/bin/python

c = [0,0]
r = [0,0]
cl = ["0,0"]
j = 0
with open('input', 'r') as f:
	while True:
		i = f.read(1)
		if not i:
			break
		for x in i:
			j+=1
			if x == ">":
				if j % 2 == 0:
					c[0]+=1
				else:
					r[0]+=1
			if x == "<":
				if j % 2 == 0:
					c[0]-=1
				else:
					r[0]-=1					
			if x == "^":
				if j % 2 == 0:
					c[1]+=1
				else:
					r[1]+=1
			if x == "v":
				if j % 2 == 0:
					c[1]-=1
				else:
					r[1]-=1
			if j % 2 == 0:
				cl.append(str(c[0])+","+str(c[1]))
			else:
				cl.append(str(r[0])+","+str(r[1]))
print len(set(cl)) 
