import csv
train_data   = []  ## set of 200 train data
test_data    = []  ## set of 200 test  data
train_label  = []  ## set of 200 train label data
test_label   = []  ## set of 200 test  label data

female_probality = []
male_probability = []

female = 0
male = 0

def read_csv_data(filename):
    try:
        buffer = None
        count = 0
        with open(filename) as csvfile:
            buffer = csv.reader(csvfile, delimiter=',')
            for row in buffer:
                temp =[]
                count = count + 1
                for item in row:
                    temp.append(float(item))
                if count <201:
                    train_data.append(temp)
                else:
                    test_data.append(temp)
    except csv.Error:
        print(f'Error reading {filename}')

def read_label_data(filename):
    try:
        buffer = None
        count = 0
        with open(filename) as csvfile:
            buffer = csv.reader(csvfile, delimiter=',')
            for row in buffer:
                count = count + 1
                if count < 201:
                    train_label.append(int(row[0]))
                else:
                    test_label.append(int(row[0]))
    except csv.Error:
        print(f'Error reading {filename}')

def label_data_probability():
    global  female
    global  male
    for item in train_label:
       if item == 1:
           female = female +1
       else:
           male = male + 1
    female = female / len(train_data)
    male = male / len(train_data)

def list_mean(numbers):
    total = 0
    for item in numbers:
        total = total +item
    total = total / (len(numbers))
    return total

def varyans(numbers):
    mean = list_mean(numbers)
    total = 0
    number_size = len(numbers)-1
    for item in numbers:
        total += (((item-mean)*(item-mean))/number_size)
    print (f'Varyans {total}')

if __name__ == '__main__':
    data =[5,5,8,12,15,18]
    varyans(data)
    read_csv_data("hw01_images.csv")
    read_label_data("hw01_labels.csv")
    label_data_probability()
    print(f'Global Female= {female} Male= {male}')
    print(f"Train data size = {len(train_data)}  First data = {train_data.__getitem__(0)} ")
    print(f"Test data size  = {len(test_data)}   First data = {test_data.__getitem__(0)} ")

    print(f"Train Label data size  = {len(train_label)}  {train_label}")
    print(f"Test  Label data size  = {len(test_label)}  {test_label}")



