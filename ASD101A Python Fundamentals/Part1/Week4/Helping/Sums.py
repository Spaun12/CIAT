repeat = 'y'

while repeat == 'y':
    num1 = int(input('Enter your first number: '))
    num2 = int(input('Enter your second number: '))
    total = num1 + num2
    print('The sum of', num1, 'and', num2, 'is:', total)
    repeat = input("Do you want to enter two more numbers? (y/n)")
    if repeat != 'y':
        print("Goodbye")


   
   

