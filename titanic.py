import csv as csv
import numpy as np
import matplotlib as plt 



csv_file = csv.reader(open('titanic/train.csv','r'))

header = next(csv_file)

data=[]

for row in csv_file:
	data.append(row[0:])
data = np.array(data)

print(data)


number_of_passengers = np.size(data[0::,1].astype(np.float))
number_survived = np.sum(data[0::,1].astype(np.float))


survival_rate = number_survived/number_of_passengers

print('survival rate is %s' %survival_rate)

number_male = data[0::,4] != 'female'
numbe_female = data[0::,4] == 'female'

men_only = data[number_male,1].astype(np.float)
women_only = data[numbe_female,1].astype(np.float)


women_survived = (np.sum(women_only)/np.size(women_only))
men_survived = (np.sum(men_only)/np.size(men_only))

print('the percentage of men that survived is %s' %men_survived)
print('the percentage of women that survived is %s' %women_survived)




testf = open('titanic/test.csv','r')
test_object = csv.reader(testf)
header = next(test_object)

predictions_file = open ("titanic/menvwomensurvival.csv", "w")
predictions_file_obj = csv.writer(predictions_file)
predictions_file_obj.writerow(["PassengerId," "Survived"])
for row in test_object:
	if row[3] == 'female':
		predictions_file_obj.writerow([row[0],"1"])
	else:
		predictions_file_obj.writerow([row[0], "0"])
testf.close()
predictions_file.close()

