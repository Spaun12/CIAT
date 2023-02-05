#Week4 Assignment AW Q4 MichaelConnell

#Write a loop that asks the user to enter a number. The loop should iterate 10 times.
#Each time the loop runs, it should ask the user to enter a number.
#After the loop has completed, the program should display the total of the numbers entered.

# Initialize a variable to store the running total
total = 0

# Initialize a variable to store the running total
total = 0

print("Note: The numbers will be rounded.")
# Use a for loop to iterate 10 times
for _ in range(10):
    # Ask the user to enter a number
    num = float(input("Enter a number: "))
    # Round the number
    num = round(num)
    # Add the rounded number to the running total
    total += num

# Print the final total of all numbers entered
print("The total of all numbers entered is:", total)




