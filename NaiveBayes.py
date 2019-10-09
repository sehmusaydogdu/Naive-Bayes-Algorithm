import csv
trainData =[]
binaryData=[]

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

def convert_data_binary():
    for list in trainData:
        temp=[]
        for item in list:
            if item < 0.5:
                temp.append(0)
            else:
                temp.append(1)
        binaryData.append(temp)

if __name__ == '__main__':
    read_csv_data("hw01_images.csv")
    convert_data_binary()
