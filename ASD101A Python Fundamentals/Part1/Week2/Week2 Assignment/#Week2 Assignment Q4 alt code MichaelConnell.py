#Week2 Assignment Q4 alt code MichaelConnell

A_score = 90
B_score = 80
C_score = 70
D_score = 60

# User input of score
score = int(input("Enter the student's score: "))  

# Execute and print
if score >= A_score:
    print('Your grade is A with score range 90-100.')
elif score >= B_score:
    print('Your grade is B with score range 80-89.')
elif score >= C_score:
    print('Your grade is C with score range 70-79.')
elif score >= D_score:
    print('Your grade is D with score range 60-69.')
else:
    print('Your grade is F with score range below 60.')
