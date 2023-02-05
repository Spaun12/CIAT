#Bugs Collected

# initialize total bugs to 0
total_bugs = 0

# ask user for number of bugs collected for each day
for i in range(5):
    bugs = int(input(f"Enter the number of bugs collected on day {i+1}: "))
    total_bugs += bugs

# print the total number of bugs collected
print("Total bugs collected:", total_bugs)
