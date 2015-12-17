#!/bin/python

with open('input', 'r') as f:
	while True:
                c = f.readlines()
                gt = 0
                wr = 0
                if not c:
                        break
                for line in c:
                        l, w, h = line.split("x")
                        sa = int(l)*int(w)
                        sb = int(w)*int(h)
                        sc = int(h)*int(l)
                        a = 2*sa + 2*sb + 2*sc
                        sm = sc
                        if (sa < sb and sa < sc):
	                        sm = sa
                        elif(sb < sc):
                                sm = sb
			arr = [int(l), int(w), int(h)]
			smn = min(arr)
			ssm = arr.remove(min(arr))
			smm = min(arr)
                        t = a + sm
                        gt = gt + t
                        sp = smn + smn + smm + smm
                        sv = int(l)*int(w)*int(h)
			wr = wr + sp + sv
		print "Total Square Feet of Wrapping Paper:", gt, "Total Ribbon Length:", wr,
