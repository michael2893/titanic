import csv as csv
import numpy as np
import matplotlib.pyplot as plt



csv_file = csv.reader(open('titanic/train.csv','r'))

header = next(csv_file)

data=[]

for row in csv_file:
	data.append(row[0:])
data = np.array(data)

tickets_sold = np.size(data[0::,2].astype(np.float))
print('tickets sold %s' %tickets_sold)

number_of_passengers = np.size(data[0::,1].astype(np.float))
first_class = data[0::,2].astype(np.float) == 1
first_class_array = data[first_class,1].astype(np.float)
first_class_only = np.size(data[first_class,1].astype(np.float))

second_class = data[0::,2].astype(np.float)== 2
second_class_only = np.size(data[second_class,1].astype(np.float))

third_class = data[0::,2].astype(np.float)== 3
third_class_only = np.size(data[third_class,1].astype(np.float))

print('first class ticket number is %s' %first_class_only)
print('second class ticket number is %s' %second_class_only)
print('third class ticket number is %s' %third_class_only)


number_male = data[0::,4] != 'female'
numbe_female = data[0::,4] == 'female'

number_survived = np.sum(data[0::,1].astype(np.float))


survival_rate = number_survived/number_of_passengers



number_male = data[0::,4] != 'female'
numbe_female = data[0::,4] == 'female'

men_only = data[number_male,1].astype(np.float)
women_only = data[numbe_female,1].astype(np.float)


women_survived = (np.sum(women_only)/np.size(women_only))
men_survived = (np.sum(men_only)/np.size(men_only))

women_only_size = np.size(women_only)
men_only_size = np.size(men_only)

women_only_sum = np.size(women_only)
men_only_sum = np.size(men_only)

women_survived_sum = women_survived * women_only_sum

men_survived_sum = men_survived * men_only_sum

# print(women_only)
# print(first_class_array)

# if women_only_size > first_class_only:
# 	print(np.size(women)	
survivor_number = survival_rate * number_of_passengers

percent_first_class = first_class_only/tickets_sold
percent_second_class = second_class_only/tickets_sold
percent_third_class = third_class_only/tickets_sold


percent_women = women_only_size/number_of_passengers
percent_men = men_only_size/number_of_passengers

women_first_class = (percent_first_class*percent_women)
women_first_class_sum = women_first_class * number_of_passengers
first_class_women_survivors = (women_first_class_sum/survivor_number)


women_second_class = (percent_second_class*percent_women)
women_second_class_sum =women_second_class * number_of_passengers
second_class_women_survivors = women_second_class_sum/survivor_number

third_class_women = (percent_third_class*percent_women)
third_class_women_sum = third_class_women* number_of_passengers
third_class_women_survivors = third_class_women_sum/survivor_number




men_first_class = percent_first_class * percent_men
men_first_class_sum = men_first_class * number_of_passengers
first_class_men_survivors = (men_first_class_sum/survivor_number)

men_second_class = percent_second_class * percent_men
men_second_class_sum = men_second_class * number_of_passengers
second_class_men_survivors = (men_second_class_sum/survivor_number)


men_third_class = percent_third_class * percent_men
men_third_class_sum = men_third_class * number_of_passengers
third_class_men_survivors = (men_third_class_sum/survivor_number)





print('women survivors: %s ' %women_survived_sum)
print('the number of women %s ' %women_only_sum)
print('men survived: %s ' %men_survived_sum)
print('the number of men %s ' %men_only_sum)



print('the percentage of tickets that are first class is %s' %percent_first_class)
print('percent of passengers that are women is %s' %percent_women)
print('the percent of first class traveling women is %s' %women_first_class)
print('survival rate is %s' %survival_rate)
print('-------------------------------------------------------------------------------')
print('the probability of dying as a first class holding women is %s' %women_first_class)
print('-------------------------------------------------------------------------------')
print('the probability of dying as a second class holding women is %s' %women_second_class)
print('-------------------------------------------------------------------------------')
print('the probability of dying as a third class holding women is %s' %third_class_women)
print('-------------------------------------------------------------------------------')
print('the probability of dying as a first class holding man is %s' %men_first_class)
print('-------------------------------------------------------------------------------')
print('the probability of dying as a second class holding man is %s' %men_second_class)
print('-------------------------------------------------------------------------------')
print('the probability of dying as a third class holding man is %s' %men_third_class)



## given that women survive more, and third class women survived more, what does that say about the 
## demographic of women?

label1 = 'Death rates based on ticket class'
label = ['first class women', 'second class women','third class women',
'first class men','second class men', 'third class men']
classes = [first_class_women_survivors, second_class_women_survivors, third_class_women_survivors,
first_class_men_survivors,second_class_men_survivors,third_class_men_survivors]
index = np.arange(len(label))
plt.bar(index, classes)
plt.xlabel('Classes', fontsize=5)
plt.ylabel('rate', fontsize=10)
plt.xticks(index, label, fontsize=5, rotation=5)
plt.title(label1)
plt.show()


label1 = 'Survival rates based on ticket class'
label = ['first class women', 'second class women','third class women',
'first class men','second class men', 'third class men']
classes = [1 -first_class_women_survivors, 1 -second_class_women_survivors, 1 -third_class_women_survivors,
1 -first_class_men_survivors,1 -second_class_men_survivors,1 -third_class_men_survivors]
index = np.arange(len(label))
plt.bar(index, classes)
plt.xlabel('Classes', fontsize=5)
plt.ylabel('rate', fontsize=10)
plt.xticks(index, label, fontsize=5, rotation=5)
plt.title(label1)
plt.show()

#it seems like more women survived, but ticket price had more of an impact on the survival of men

men_survived_array=[]

for row in csv_file:
	if row[2]=='male':
		data.append(row[0:])
men_survived_array = np.array(men_survived_array)


print(' men survived array%s ' %men_survived_array)

# np.corrcoef(men)


# second class women more redady to get hands 'dirty' make a ds for this

#  not first not last in middle, no what its' like to want for, but don't not have

#socio cultural "ladisl" 


		
