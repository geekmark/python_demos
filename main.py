#!/usr/bin/env python
import matplotlib.pyplot as plt

input = open('./caffe.log', 'r')

lossval = [0.0]
cnt = 0

for line in input:
#    cnt = cnt+1 
#    print cnt
    line = line.split()
    if "solver.cpp:239]" in line:
#	print line
        lossval.append(float(line[-1]))

plt.figure('loss val')
plt.grid(True)
plt.plot(lossval)
plt.show()
