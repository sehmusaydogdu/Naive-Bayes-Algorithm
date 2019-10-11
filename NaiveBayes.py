import csv
import math

train_data   = []  ## set of 200 train data
test_data    = []  ## set of 200 test  data
train_label  = []  ## set of 200 train label data
test_label   = []  ## set of 200 test  label data
transponse=[]

female_probability = []
male_probability = []

female = 0  ## 0.1
male = 0    ## 0.9

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

def train_label_probability():
    global  female
    global  male
    for item in train_label:
       if item == 1:
           female = female +1
       else:
           male = male + 1
    female = female / len(train_data)
    male = male / len(train_data)

def probability_table(numbers):
    female_list =[]
    male_list   =[]

    female_temp =[]
    male_temp=[]

    for index in range(len(numbers)):
        if train_label[index] == 1:
            female_list.append(numbers[index])
        else:
            male_list.append(numbers[index])

    female_mean = list_mean(female_list)
    female_varyans = list_varyans(female_list,female_mean)
    female_temp.append(female_mean)
    female_temp.append(female_varyans)
    print(f'Female Mean = {female_mean}  Varyans ={female_varyans} ')
    female_probability.append(female_temp)

    male_mean = list_mean(male_list)
    male_varyans = list_varyans(male_list,male_mean)
    male_temp.append(male_mean)
    male_temp.append(male_varyans)
    print(f'Male Mean = {male_mean}  Varyans ={male_varyans} ')
    male_probability.append(male_temp)

def list_mean(numbers):
    total = 0
    lenght = (len(numbers))
    for item in numbers:
        total = total +item
    total = total / lenght
    return total

def list_varyans(numbers,mean):
    total = 0
    number_size = len(numbers)
    for item in numbers:
        total += (((item-mean)*(item-mean))/number_size)
    return math.sqrt(total);

def transponse_matrix():
    transpose = list(zip(*train_data))
    for row in transpose:
        probability_table(row)

if __name__ == '__main__':
    read_csv_data("hw01_images.csv")
    read_label_data("hw01_labels.csv")

    train_label_probability()
    transponse_matrix()

    print(f'Global Female= {female} Male= {male}')
    print(f'Train data size = {len(train_data)}')
    print(f'Test data size  = {len(test_data)} ')

    print(f"Train Label data size  = {len(train_label)}  {train_label}")
    print(f"Test  Label data size  = {len(test_label)}  {test_label}")



