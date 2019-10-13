import csv
import math
import statistics

images_data=[]   ## Program ilk açıldığında "hw01_images.csv" dosyasının içeriği okur ve değişkene atar.
label_data=[]    ## Program ilk açıldığında "hw01_label.csv" dosyasının içeriği okur ve değişkene atar.

training=[]  ## "hw01_images.csv" dosyasıdaki ilk 200 veriyi training olarak belirledim
test=[]     ## "hw01_images.csv" dosyasıdaki diğer 200 veriyi test olarak belirledim

label_training=[]   ## "hw01_label.csv" dosyasıdaki ilk 200 veriyi training olarak belirledim
label_test=[]       ## "hw01_label.csv" dosyasıdaki diğer 200 veriyi test olarak belirledim

female=[]
male=[]

def deviation(mean,values):
    result = 0
    for index in range(len(values)):
        result += (math.pow((values[index]-mean),2))
    result = math.sqrt(result / len(values))
    return result

def gauss(x,mean,deviation):
    return (1.0/(deviation*math.sqrt(2.0*math.pi)))*math.exp((-1.0)*math.pow((x-mean),2.0)/(2.0*math.pow(deviation,2.0)))

def log_probability(values):
  sum = 0.0
  for item in values:
      sum = sum + math.log(item,math.e)
  return sum

def images_data_read(filename):
    reader= None
    with open(filename, 'r') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            images_data.append(row)
    csvFile.close()

def images_data_split():
    ## trainig data
    for i in range(0,200):
        dummy=[]
        for item in images_data[i]:
            dummy.append(float(item))
        training.append(dummy)

    ##test data
    for i in range(200,400):
        dummy=[]
        for item in images_data[i]:
            dummy.append(float(item))
        test.append(dummy)

def label_data_read(filename):
    reader= None
    with open(filename, 'r') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            label_data.append(row)
    csvFile.close()

def label_data_split():
    ## trainig data
    for i in range(0, 200):
        for item in label_data[i]:
            label_training.append(int(item))

    ##test data
    for i in range(200, 400):
        for item in label_data[i]:
            label_test.append(int(item))

def female_probability():
    count = 0.0
    for data in label_training:
        if data == 1:
            count = count + 1
    return count / len(label_training)

def male_probability():
    count = 0.0
    for data in label_training:
        if data == 2:
            count = count + 1
    return count / len(label_training)

def training_calc():
    matrix = list(zip(*training))
    for numbers in matrix:
        female_and_male_pro_calc(numbers)

def female_and_male_pro_calc(numbers):
    female_dummy=[]
    female_list =[]

    male_dummy=[]
    male_list=[]

    for i in range(len(numbers)):
        if label_training[i] == 1:
            female_list.append(numbers[i])
        else:
            male_list.append(numbers[i])

    mean1 = statistics.mean(female_list)
    dev1 = deviation(mean1,female_list)
    print(f'FEMALE {mean1}  {dev1} ')

    female_dummy.append(mean1)
    female_dummy.append(dev1)
    female.append(female_dummy)

    mean2=statistics.mean(male_list)
    dev2=deviation(mean2,male_list)
    print(f'MALE {mean2}  {dev2} ')

    male_dummy.append(mean2)
    male_dummy.append(dev2)
    male.append(male_dummy)

def training_confusion(data,f,m):
    list=[]
    for i in range(len(data)):
        female_calc = []
        male_calc = []

        for j in range(len(data[i])):
            female_calc.append(gauss(data[i][j], female.__getitem__(i)[0], female.__getitem__(i)[1]))
            male_calc.append  (gauss(data[i][j],male.__getitem__(i)[0], male.__getitem__(i)[1]))

        f_sum_log = log_probability(female_calc) + math.log(f)
        m_sum_log = log_probability(male_calc) + math.log(m)

        if f_sum_log > m_sum_log:
            list.append(1)
        else:
            list.append(2)
    return list

def calculator_confisuon_matrix(expected,actual):
    matrix = [[0, 0], [0, 0]]
    for index in range(len(expected)):
        if expected[index] == 1 and actual[index] ==1:
            matrix[0][0] +=1
        if expected[index] == 1 and actual[index] ==2:
            matrix[0][1] +=1
        if expected[index] == 2 and actual[index] ==1:
            matrix[1][0] +=1
        if expected[index] == 2 and actual[index] ==2:
            matrix[1][1] += 1
    return matrix


images_data_read("hw01_images.csv")
images_data_split()

label_data_read("hw01_labels.csv")
label_data_split()

female_prob = female_probability()
male_prob = male_probability()

training_calc()

expected_train_list= training_confusion(training,female_prob,male_prob)
expected_test_list = training_confusion(test,female_prob,male_prob)

print(f"Training = {calculator_confisuon_matrix(expected_train_list,label_training)}")
print(f"Test     = {calculator_confisuon_matrix(expected_test_list,label_test)}")

print(f'Priors ={female_prob} {male_prob}')



