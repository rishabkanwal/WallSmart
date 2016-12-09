import sys
import math
import random

with open(sys.argv[2],'r') as source:
    data = [(random.random(), line) for line in source]
data.sort()

lastLine = math.floor(float(sys.argv[1]) * len(data))


with open(sys.argv[3],'w') as target1:
    for i in range(lastLine):
        line = data[i][1]
        if line.strip():
            target1.write(line)

if float(sys.argv[1]) < 1.0:
	with open(sys.argv[4],'w') as target2:
	    for i in range(lastLine, len(data)):
	        line = data[i][1]
	        if line.strip():
	            target2.write(line)

