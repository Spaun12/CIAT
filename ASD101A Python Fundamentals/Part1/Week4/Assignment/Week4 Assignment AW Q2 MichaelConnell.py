# Week4 Assignment AW Q2 MichaelConnell

while True:
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    sum = float(num1) + float(num2)
    print("The sum is: ", sum)
    repeat = input("Do you want to perform the operation again? (yes/no)")
    if repeat.lower() == "no":
        break
