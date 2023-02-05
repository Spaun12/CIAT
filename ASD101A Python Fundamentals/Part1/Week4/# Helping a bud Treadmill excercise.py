# Helping a bud Treadmill excercise

#created variables and equations
treadmill = 4.2

#control loop
another = 'y'

#table heading
print ('The calories burned every 5 min is displayed for the first 30 min.')
print ('Time\tCalories burned')
print ('------------------------')

#print the numbers for every 5 minutes from 5 to 30
for time in range(5, 31, 5):
    calories = treadmill * time
    print (f'{time}\t {calories:,.2f}')

#loop to get input from user and print the number of calories burned
while another == 'y' or another == 'Y':
    time = float(input('Enter the time in minutes that you plan to run today. Up to 30 minutes.: '))
    calories = treadmill * time #calculate calories burned based on user input
    print (f'Your plan is to burn {calories:,.2f} calories in {time} minutes on the treadmill.')
    #repeat if so desired
    another = input('Do you want to enter another time? (y/n): ')
