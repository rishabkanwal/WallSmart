import time

# This While loop creates a dictionary with store information
def parse_stores_csv():
    i = 0
    store_labels = []
    stores = {}
    with open('stores.csv') as data:
        for line in data:
            formatted = line.strip().split(',')
            # print formatted
            if i == 0:
                for feature in range(0, len(formatted)):
                    store_labels.append(formatted[feature])
            else:
                # print formatted
                stores[formatted[0]] = {};
                stores[formatted[0]][store_labels[1]] = formatted[1]
                stores[formatted[0]][store_labels[2]] = formatted[2]
            i += 1
    # print stores
    return stores


def build_train():
    i = 0
    labels = []
    stores = parse_stores_csv()
    # This while loop
    with open('test_stores.vw', 'w') as target:
        with open('test.csv') as data:
            for line in data:
                formatted = line.rstrip('\n').split(',')
                if i == 0:
                    for i in range(0, len(formatted)):
                        labels.append(formatted[i])
                else:
                    output = "1 | "
                    for feature in range(0, len(formatted)):
                        if feature == 3:
                            continue
                        elif feature == 2:
                            parsed_date = formatted[feature].split("-")
                            # print parsed_date
                            year = str(int(parsed_date[0]) - 2010)
                            output += "Year:" + year + " "
                            day_in_year = str(time.strptime(formatted[feature],"%Y-%m-%d").tm_yday)
                            output += "Day:" + day_in_year + " "
                        elif feature == 4:
                            if formatted[feature] == "FALSE":
                                output += labels[feature] + ":0 "
                            else:
                                output += labels[feature] + ":1 "
                        else:
                            output += labels[feature] + ":" + formatted[feature] + " "
                            if feature == 0:
                                for key in stores[formatted[feature]]:
                                    # print key
                                    output += key + ":" + stores[formatted[feature]][key] + " "
                    target.write(output + "\n")
                i += 1

def main():
    build_train()

if __name__ == "__main__":
    main()
