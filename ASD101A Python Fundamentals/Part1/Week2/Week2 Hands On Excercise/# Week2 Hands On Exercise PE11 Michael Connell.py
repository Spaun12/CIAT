# Week2 Hands On Exercise PE11 Michael Connell
# Get the number of males and females
num_males = int(input("Enter the number of males: "))
num_females = int(input("Enter the number of females: "))

# Calculate the total number of students
total_students = num_males + num_females

# Calculate the percentage of males and females
percent_males = num_males / total_students
percent_females = num_females / total_students

# Print the results
print("Percentage of males: {:.2f}".format(percent_males * 100))
print("Percentage of females: {:.2f}".format(percent_females * 100))
