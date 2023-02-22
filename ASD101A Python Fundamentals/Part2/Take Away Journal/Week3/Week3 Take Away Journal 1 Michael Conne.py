#Week3 Take Away Journal 1 Michael Connell

# Accept user input for the string
my_string = input("Enter a string: ")

# Access individual characters using indexing
print("First character: {}".format(my_string[0]))
print("Third character: {}".format(my_string[2]))

# Extract a portion of the string using slicing
print("First five characters: {}".format(my_string[0:5]))
print("Last five characters: {}".format(my_string[-5:]))

# String formatting with user input
name = input("Enter your name: ")
age = input("Enter your age: ")
print(f"My name is {name} and I'm {age} years old.")
