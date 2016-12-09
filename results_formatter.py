import sys
import linecache

i = 0
labels = []
with open(sys.argv[3], 'w') as target:
    with open(sys.argv[2]) as test:
        with open(sys.argv[1]) as predictions:
            target.write("Id,Weekly_Sales" + "\n")
            for i,line in enumerate(test):
                if i == 0:
                    continue
                else:
                    stripped = line.rstrip('\n').split(',')
                    predicted = str(round(float(linecache.getline(sys.argv[1], i)), 2))
                    output = stripped[0] + "_" + stripped[1] + "_" + stripped[2] + "," + predicted
                target.write(output + "\n")

