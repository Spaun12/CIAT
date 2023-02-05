#Week2: Hands On Exercise 11 MichaelConnell

#Input Number of Males and Females in Class
num_males = int(input("Enter the number of males in the class: "))
num_females = int(input("Enter the number of females in the class: "))
total_students = num_males + num_females

#Calculate Percentage of each
male_percentage = num_males / total_students * 100
female_percentage = num_females / total_students * 100

#Display Results
print("The percentage of males in the class is {:.2f}%".format(male_percentage))
print("The percentage of females in the class is {:.2f}%".format(female_percentage))