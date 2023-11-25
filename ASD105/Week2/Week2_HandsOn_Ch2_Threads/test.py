result = 0
for i in range(10):
    if i % 2 == 0:
        result += i  # Adding even numbers to 'result'
    else:
        result -= i  # Subtracting odd numbers from 'result'

print("Final result:", result)  # Output the value of 'result'
