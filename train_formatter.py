import sys
import time

def convertLetter(letter):
    if letter == 'A':
        return 1
    elif letter == 'B':
        return 2
    else:
        return 3

# This While loop creates a dictionary with store information
def parse_stores_csv():
    i = 0
    store_labels = []
    stores = {}
    with open(sys.argv[2]) as data:
        for line in data:
            formatted = line.strip().split(',')
            if i == 0:
                for feature in range(0, len(formatted)):
                    store_labels.append(formatted[feature])
            else:
                stores[formatted[0]] = {};
                stores[formatted[0]][store_labels[1]] = convertLetter(formatted[1])
                stores[formatted[0]][store_labels[2]] = formatted[2]
            i += 1
    return stores

def parse_features_csv():
    i = 0
    feature_labels = []
    features = {}
    with open(sys.argv[3]) as data:
        for line in data:
            formatted = line.strip().split(',')
            if i == 0:
                for feature in range(0, len(formatted)-1):
                    feature_labels.append(formatted[feature])
            else:
                for feature in range(0, len(feature_labels)):
                    if feature == 0:
                        if formatted[0] not in features:
                            features[formatted[0]] = {}
                    elif feature == 1:
                        features[formatted[0]][formatted[1]] = {}
                            # features[formatted[0]][formatted[1]]["MarkDown"] = 0
                    else:
                        features[formatted[0]][formatted[1]][feature_labels[feature]] = formatted[feature]
            i += 1
    return features

def build_train(doFeatures, doStores):
    i = 0
    labels = []
    stores = ""
    features = ""
    if doStores:
        stores = parse_stores_csv()
    if doFeatures: 
        features = parse_features_csv()
    # This while loop
    with open(sys.argv[4], 'w') as target:
        with open(sys.argv[1]) as data:
            for line in data:
                formatted = line.rstrip('\n').split(',')
                if i == 0:
                    for i in range(0, len(formatted)):
                        labels.append(formatted[i])
                else:
                    output = formatted[3] + " | "
                    for feature in range(0, len(formatted)):
                        if feature == 3:
                            continue
                        elif feature == 2:
                            parsed_date = formatted[feature].split("-")
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
                                if doStores:
                                    for key in stores[formatted[feature]]:
                                        # print key
                                        output += key + ":" + str(stores[formatted[feature]][key]) + " "
                                if doFeatures:
                                    for key in features[formatted[feature]][formatted[2]]:
                                        key_val = features[formatted[feature]][formatted[2]][key]
                                        if key_val == "NA":
                                            key_val = 0
                                        output += key + ":" + str(key_val) + " "
                    target.write(output + "\n")
                i += 1

def main():
    if not (len(sys.argv) >= 5 and len(sys.argv) <= 6):
        print('Usage: python train_formatter.py <Train file> <Store file> <Features File> <Output file>')
        return
    if len(sys.argv) == 5:
        build_train(False, False)
    elif len(sys.argv) == 6:
        if sys.argv[5] == '-f':
            build_train(True, False)
        elif sys.argv[5] == '-s':
            build_train(False, True)
        elif sys.argv[5] == '-fs':
            build_train(True, True)


if __name__ == "__main__":
    main()
