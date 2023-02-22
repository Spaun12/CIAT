# Define a string with some punctuation
my_string = "Hello, World! How are you doing?"

# Define a string of punctuation characters
punctuation = "!@#$%^&*()_-+={}[]|\:;\"'<>,.?/~`"

# Replace each punctuation character with an empty string
for char in punctuation:
    my_string = my_string.replace(char, "")

# Print the resulting string with punctuation removed
print(my_string)
