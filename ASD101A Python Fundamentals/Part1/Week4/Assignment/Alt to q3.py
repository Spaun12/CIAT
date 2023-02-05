# Alt to q3

# Initialize a counter variable to 1
counter = 1

# Use a for loop to iterate through the range of numbers from 0 to 1000, in increments of 10
for i in range(0, 1010, 10):
    # Print the current numbers and add a comma with space at the end of each
    print(i, end=', ')
    
    # Check if the counter is divisible by 10 and designates the numbers in the row
    if counter % 10 == 0:
        # If it is, print a new line
        print()
    # Increase the counter/row by 1
    counter += 1
