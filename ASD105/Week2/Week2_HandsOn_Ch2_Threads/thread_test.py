# Michael Connell Week2 Hands-On Ch2 Threads
# Date: 2023-10-21
# Import the threading module
import threading

# Define a function to print numbers from 0 to 9
def print_nums():
    for i in range(10):
        print(i)

# Define a function to print characters from 'a' to 'j'
def print_chars():
    for i in range(97, 107):
        print(chr(i))

# Create two threads, one for each function
thread1 = threading.Thread(target=print_nums)
thread2 = threading.Thread(target=print_chars)

# Start the threads
thread1.start()
thread2.start()

# Wait for the threads to finish
thread1.join()
thread2.join()

# Print a message indicating the end of the program
print("End of Program")

# Predicted Output for the initial run:
# 0
# a
# 1
# b
# 2
# c
# 3
# d
# 4
# e
# 5
# f
# 6
# g
# 7
# h
# 8
# i
# 9
# j
# End of Program

