import linecache

i = 0
labels = []
with open('results.vw', 'w') as target:
    with open('test.csv') as test:
        with open('predictions.txt') as predictions:
            target.write("Id,Weekly_Sales" + "\n")
            for i,line in enumerate(test):
                if i == 0:
                    continue
                else:
                    stripped = line.rstrip('\n').split(',')
                    predicted = str(round(float(linecache.getline('predictions.txt', i)), 2))
                    output = stripped[0] + "_" + stripped[1] + "_" + stripped[2] + "," + predicted
                target.write(output + "\n")

