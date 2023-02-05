#Week4 Hand On Programming Exercis 2 MichaelConnell

# define the number of calories burned per minute for each treadmill
dragon_treadmill = 14.2
donkey_treadmill = 4.2
panda_treadmill = 2.8

while True:
    # ask the user to select a treadmill
    user_input = input("Which treadmill are you going to use? (Dragon, Panda, Donkey): ")
    if user_input.lower() == "dragon":
        calories_burned_per_minute = dragon_treadmill
    elif user_input.lower() == "panda":
        calories_burned_per_minute = panda_treadmill
    elif user_input.lower() == "donkey":
        calories_burned_per_minute = donkey_treadmill
    else:
        print("Invalid input. Please select Dragon, Panda, or Donkey.")
        continue
    
    # use a for loop to iterate through the number of minutes
    for minutes in [10, 15, 20, 25, 30]:
        # calculate the number of calories burned
        calories_burned = minutes * calories_burned_per_minute
        # print the number of calories burned
        print(f"After {minutes} minutes, you wil have burned {calories_burned} calories.")
    
    # ask the user if they are done or want to see results for a different treadmill
    user_input = input("Are you done? (yes/no)")
    if user_input.lower() == "yes":
        break

