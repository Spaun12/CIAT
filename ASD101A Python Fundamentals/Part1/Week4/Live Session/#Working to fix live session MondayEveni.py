#Working to fix live session MondayEvening_Excercise 1 MichaelConnell

# Step 1: Initialize tire inventory
auto_tires = int(input("Enter number of auto tires in inventory: "))
truck_tires = int(input("Enter number of truck tires in inventory: "))

# Step 2: Enter while loop for tire sales
while True:
    try:
        # Step 3: Prompt user for tire selection and check for valid input
        sales = int(input("""
                    What type of tires would you like
                    to purchase? Please enter the
                    number associated with the type
                    of tires:

                    1) Auto Tires
                    2) Truck Tires

                    Enter your selection: """))
    except ValueError:
        print("Invalid selection. Please enter a number.")
        continue

    if sales == 1:
        tire_type = "auto"
        tire_inventory = auto_tires
    elif sales == 2:
        tire_type = "truck"
        tire_inventory = truck_tires
    else:
        print("Invalid selection. Please try again.")
        continue

    # Step 4: Check if inventory is available
    if tire_inventory <= 0:
        print(f"There are no {tire_type} Tires left in inventory.")
        print("We will contact you when we have replenished our inventory.")
        print("Sorry for any inconvenience!")
        break
    
    try:
        # Step 5: Prompt user for number of tires to purchase and check for valid input
        tire_sales = int(input(f"Enter number of {tire_type} tires purchased: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue
        
    if tire_sales > tire_inventory:
        print(f"There are only {tire_inventory} {tire_type} Tires left in inventory.")
        adjust = input("Would you like to adjust your order? (Y/N)").lower()
        if adjust == 'y':
            continue
        else:
            break
    tire_inventory -= tire_sales
    print(f"You've purchased {tire_sales} {tire_type} Tires.")
    print(f"{tire_type} Tires inventory is now set to {tire_inventory}.")
    if tire_inventory <= 0:
        print(f"There are no {tire_type} Tires left in inventory.")
        print("We will contact you when we have replenished our inventory.")
        print("Sorry for any inconvenience!")
        break
    # Step 6: Prompt user to finish ordering and check for valid input
    OrderFinished = input("Are you finished ordering? (Y/N)").lower()
    if OrderFinished == 'y':
        break
    elif OrderFinished != 'n':
        print("Invalid input. Please enter 'Y' or 'N'.")








