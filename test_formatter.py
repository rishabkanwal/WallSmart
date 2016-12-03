import time

i = 0
labels = []
with open('test.vw', 'w') as target:
    with open('test.csv') as data:
        for line in data:
            formatted = line.rstrip('\n').split(',')
            if i == 0:
                for i in range(0, len(formatted)):
                    labels.append(formatted[i])
            else:
                output = "1 | "
                for i in range(0, len(formatted)):
                    if i == 2:
                        parsed_date = formatted[i].split("-")
                        print parsed_date
                        year = str(int(parsed_date[0]) - 2010)
                        output += "Year:" + year + " "
                        day_in_year = str(time.strptime(formatted[i],"%Y-%m-%d").tm_yday)
                        output += "Day:" + day_in_year + " "
                    elif i == 3:
                        if formatted[i] == "FALSE":
                            output += labels[i] + ":0 "
                        else:
                            output += labels[i] + ":1 "
                    else:
                        output += labels[i] + ":" + formatted[i] + " "
                target.write(output + "\n")
            i += 1