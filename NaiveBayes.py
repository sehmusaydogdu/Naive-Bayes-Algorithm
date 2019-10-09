import csv
trainData =[]
binaryData=[]
labelData =[]

def read_csv_data(filename):
    try:
        buffer = None
        with open(filename) as csvfile:
            buffer = csv.reader(csvfile, delimiter=',')
            for row in buffer:
                temp =[]
                for item in row:
                    temp.append(float(item))
                trainData.append(temp)
    except csv.Error:
        print(f'Error reading {filename}')

def read_label_data(filename):
    try:
        buffer = None
        with open(filename) as csvfile:
            buffer = csv.reader(csvfile, delimiter=',')
            for row in buffer:
                labelData.append(int(row[0]))
    except csv.Error:
        print(f'Error reading {filename}')

def convert_data_binary():
    for list in trainData:
        temp=[]
        for item in list:
            if item < 0.5:
                temp.append(0)
            else:
                temp.append(1)
        binaryData.append(temp)

def label_probability():
    female = 0
    male = 0
    for label in labelData:
        if label == 1:
            female = female+1
        else:
            male = male + 1

    total = len(labelData)
    female = female / total
    male = male /total
    print(f'Total label= {total} Female= {female} Male= {male}')


if __name__ == '__main__':
    read_csv_data("hw01_images.csv")
    read_label_data("hw01_labels.csv")
    convert_data_binary()
    label_probability()


