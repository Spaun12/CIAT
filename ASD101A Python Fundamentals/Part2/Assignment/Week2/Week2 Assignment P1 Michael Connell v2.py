#Week2 Assignment P1 Michael Connell v2
# assume numbers1 has 100 elements (because they do)
numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 
            16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
            29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41,
            42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54,
            55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67,
            68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
            81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93,
            94, 95, 96, 97, 98, 99, 100]  
# numbers2 is an empty list
numbers2 = []  
# use a for loop to iterate over the elements in numbers1
for num in numbers1:
    # add each element to numbers2
    numbers2.append(num)
# Define a string format for each line of the list 
# (trying to make it look like the original list)
line_format = "{:<4}" # Format specifier aligned to the left with a width of 4
# Print the list in the same shape as numbers1
print("numbers2 = [", end="") # Print the opening bracket
for i, num in enumerate(numbers2):
    if i % 15 == 0 and i != 0: # Couldn't make it look exactly like numbers1 but this is close
        print("\n           ", end="") # Print a newline and 11 spaces which took forever ;)
    # Print the number and a comma if it's not the last number
    print(line_format.format(num), end=", " if i != len(numbers2) - 1 else "]") 