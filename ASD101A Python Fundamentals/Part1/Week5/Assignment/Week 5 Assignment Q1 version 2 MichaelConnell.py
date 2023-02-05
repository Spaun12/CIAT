#Week 5 Assignment Q1 version 2 MichaelConnell
#First I will create a function that will ask the user to enter a number
#and then multiply that number by 10 and print the result
def times_ten():
    n = int(input("Enter a number: "))
    result = n*10
    print('The number times 10 is:', result)
#call the main function
times_ten()