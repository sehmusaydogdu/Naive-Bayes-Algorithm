import csv
import math

train_data   = []  ## set of 200 train data
test_data    = []  ## set of 200 test  data
train_label  = []  ## set of 200 train label data
test_label   = []  ## set of 200 test  label data

train_confusion_matrix = [[0,0],[0,0]]
test_confusion_matrix  = [[0,0],[0,0]]

female_probability = []
male_probability = []

epsilon = 0.5

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
    lenght = len(train_label)
    for item in train_label:
       if item == 1: female = female +1
       else: male = male + 1
    female = female / lenght
    male = male / lenght

def transponse_matrix():
    transpose = list(zip(*train_data))
    for row in transpose:
        probability_table(row)

def probability_table(numbers):
    female_list =[]
    male_list   =[]

    female_temp =[]
    male_temp=[]

    for index in range(len(numbers)):
        if train_label[index] == 1: female_list.append(numbers[index])
        else: male_list.append(numbers[index])

    female_mean = list_mean(female_list)
    female_deviation = list_deviation(female_list,female_mean)
    female_temp.append(female_mean)
    female_temp.append(female_deviation)
    print(f'Female Mean = {female_mean}  Deviation ={female_deviation} ')
    female_probability.append(female_temp)

    male_mean = list_mean(male_list)
    male_deviation = list_deviation(male_list,male_mean)
    male_temp.append(male_mean)
    male_temp.append(male_deviation)
    print(f'Male Mean = {male_mean}  Deviation ={male_deviation} ')
    male_probability.append(male_temp)

def multiplication(numbers):
    temp = 1.0
    for item in numbers:
        temp = (temp * item * epsilon)
    return temp

def confusion_matrix(data , label, confusion_matrix):
    lenght = len(data)
    for rowID in range(lenght):
        female_calculator = []
        male_calculator = []
        for index in range(len(data[rowID])):
            female_list = female_probability.__getitem__(index)
            female_calculator.append(gauss_formula(data[rowID][index], female_list[0], female_list[1]))

            male_list = male_probability.__getitem__(index)
            male_calculator.append(gauss_formula(data[rowID][index],male_list[0],male_list[1]))

        f_multiplaciton = multiplication(female_calculator) * female
        m_multiplaciton = multiplication(male_calculator) * male

        if(f_multiplaciton > m_multiplaciton):  ## Female
            if label[rowID] == 1:
                confusion_matrix[0][0] = confusion_matrix[0][0] + 1
            else:
                confusion_matrix[0][1] = confusion_matrix[0][1] + 1
        else: ## Male
            if label[rowID] == 1:
                confusion_matrix[1][0] = confusion_matrix[1][0] + 1
            else:
                confusion_matrix[1][1] = confusion_matrix[1][1] + 1

def gauss_formula(data,mean,deviation):
    result = (1/(deviation*math.sqrt(2*math.pi)))*math.exp((-1)*math.pow((data-mean),2)/(2*math.pow(deviation,2)))
    return result

def list_mean(numbers):
    total = 0
    lenght = len(numbers)
    for item in numbers:
        total = total +item
    total = total / lenght
    return total

def list_deviation(numbers,mean):
    total = 0
    lenght = len(numbers)
    for item in numbers:
        total += (math.pow((item-mean),2))
    total = total /lenght
    return math.sqrt(total)

if __name__ == '__main__':
    read_csv_data("hw01_images.csv")
    read_label_data("hw01_labels.csv")

    train_label_probability()
    transponse_matrix()
    print(f'Probability Female= {female} Male= {male}')

    confusion_matrix(train_data, train_label, train_confusion_matrix)
    print(train_confusion_matrix)
    print(f'Train Accuracy : {(train_confusion_matrix[0][0] + train_confusion_matrix[1][1]) / len(train_data)}')

    confusion_matrix(test_data, test_label, test_confusion_matrix)
    print(test_confusion_matrix)
    print(f'Test Accuracy : {(test_confusion_matrix[0][0] + test_confusion_matrix[1][1]) / len(test_data)}')
