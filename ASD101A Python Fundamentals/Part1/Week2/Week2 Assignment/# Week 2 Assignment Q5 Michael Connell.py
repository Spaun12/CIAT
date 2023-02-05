# Week 2 Assignment Q5 Michael Connell

# Read the values of amount1 and amount2 from user input
amount1 = int(input("Enter the value of amount1: "))
amount2 = int(input("Enter the value of amount2: "))

# Execute the if-else statement
if amount1 > 10 and amount2 < 100:
    if amount1 > amount2:
        print('amount1 is greater')
    elif amount2 > amount1:
        print('amount2 is greater')
else:
    print('Amounts not in valid range')

