# Week 4, Monday evening
# Exercise - Inventory control
# This program monitors and controls
# the number of tires in inventory

auto_tires = int(input("Enter number of auto tires in inventory: "))
truck_tires = int(input("Enter number of truck tires in inventory: "))
OrderFinished = 'y'

sales = int(input("""
                What type of tires would you like
                to purchase? Please enter the
                number associated with the type
                of tires:
                
                1) Auto Tires
                2) Truck Tires
                
                Enter your selection: """))
if sales == 1:
    while auto_tires > 0 or OrderFinished != 'y':
        auto_tire_sales = int(input("Enter number of auto tires purchased: "))
        if auto_tire_sales <= auto_tires:
            auto_tires -= auto_tire_sales
            print(f"You've purchased {auto_tire_sales} auto tires.")
            print(f"Auto Tires inventory is now set to {auto_tires}.")
            OrderFinished = input("""
                Thank you for inputting your order!
                Are you finished ordering?
                Enter Y for Yes or N for No: """).lower()
            if OrderFinished == 'n':
                sales = int(input("""
                What type of tires would you like
                to purchase? Please enter the
                number associated with the type
                of tires:
                
                1) Auto Tires
                2) Truck Tires
                
                Enter your selection: """))
                
        else:
            print(f"""
                There are only {auto_tires} Auto Tires left in inventory.
                We will contact you when we have replenished our
                Auto Tires inventory.

                Sorry for any inconvenience!
                """)
elif sales == 2:
    while truck_tires > 0 or OrderFinished != 'y':
        truck_tire_sales = int(input("Enter number of truck tires purchased: "))
        if truck_tire_sales <= truck_tires:
            truck_tires -= truck_tire_sales
            print(f"You've purchased {truck_tire_sales} truck tires.")
            print(f"Truck Tires inventory is now set to {truck_tires}.")
            OrderFinished = input("""
                Thank you for inputting your order!
                Are you finished ordering?
                
                Enter Y for Yes or N for No: """).lower()
            if OrderFinished == 'n':
                sales = int(input("""
                What type of tires would you like
                to purchase? Please enter the
                number associated with the type
                of tires:
                
                1) Auto Tires
                2) Truck Tires
                
                Enter your selection: """))
 # This is where we would need to enter the code again...
 
                if sales == 1:
                     while auto_tires > 0 or OrderFinished != 'y':
                         auto_tire_sales = int(input("Enter number of auto tires purchased: "))
                         if auto_tire_sales <= auto_tires:
                             auto_tires -= auto_tire_sales
                             print(f"You've purchased {auto_tire_sales} auto tires.")
                             print(f"Auto Tires inventory is now set to {auto_tires}.")
                             OrderFinished = input("""
                                Thank you for inputting your order!
                                Are you finished ordering?
                                Enter Y for Yes or N for No: """).lower()
                             if OrderFinished == 'n':
                                 sales = int(input("""
                                What type of tires would you like
                                to purchase? Please enter the
                                number associated with the type
                                of tires:
                                
                                1) Auto Tires
                                2) Truck Tires
                                
                                Enter your selection: """))
                             else:
                                 print("Thank you for your Tire orders!")
                                
                         else:
                             print(f"""
                                There are only {auto_tires} Auto Tires left in inventory.
                                We will contact you when we have replenished our
                                Auto Tires inventory.

                                Sorry for any inconvenience!
                                """)
                elif sales == 2:
                    while truck_tires > 0 or OrderFinished != 'y':
                        truck_tire_sales = int(input("Enter number of truck tires purchased: "))
                        if truck_tire_sales <= truck_tires:
                            truck_tires -= truck_tire_sales
                            print(f"You've purchased {truck_tire_sales} truck tires.")
                            print(f"Truck Tires inventory is now set to {truck_tires}.")
                            OrderFinished = input("""
                                Thank you for inputting your order!
                                Are you finished ordering?
                                
                                Enter Y for Yes or N for No: """).lower()
                            if OrderFinished == 'n':
                                sales = int(input("""
                                What type of tires would you like
                                to purchase? Please enter the
                                number associated with the type
                                of tires:
                                
                                1) Auto Tires
                                2) Truck Tires
                                
                                Enter your selection: """))

                            if sales == 1:
                                while auto_tires > 0 or OrderFinished != 'y':
                                auto_tire_sales = int(input("Enter number of auto tires purchased: "))
                                if auto_tire_sales <= auto_tires:
                                    auto_tires -= auto_tire_sales
                                    print(f"You've purchased {auto_tire_sales} auto tires.")
                                    print(f"Auto Tires inventory is now set to {auto_tires}.")
                                    OrderFinished = input("""
                                Thank you for inputting your order!
                                Are you finished ordering?
                                Enter Y for Yes or N for No: """).lower()
                                    if OrderFinished == 'n':
                                        sales = int(input("""
                                What type of tires would you like
                                to purchase? Please enter the
                                number associated with the type
                                of tires:
                                
                                1) Auto Tires
                                2) Truck Tires
                                
                                Enter your selection: """))
                             else:
                                 print("Thank you for your Tire orders!")
                                
                         else:
                             print(f"""
                                There are only {auto_tires} Auto Tires left in inventory.
                                We will contact you when we have replenished our
                                Auto Tires inventory.

                                Sorry for any inconvenience!
                                """)
                elif sales == 2:
                    while truck_tires > 0 or OrderFinished != 'y':
                        truck_tire_sales = int(input("Enter number of truck tires purchased: "))
                        if truck_tire_sales <= truck_tires:
                            truck_tires -= truck_tire_sales
                            print(f"You've purchased {truck_tire_sales} truck tires.")
                            print(f"Truck Tires inventory is now set to {truck_tires}.")
                            OrderFinished = input("""
                                Thank you for inputting your order!
                                Are you finished ordering?
                                
                                Enter Y for Yes or N for No: """).lower()
                            if OrderFinished == 'n':
                                sales = int(input("""
                                What type of tires would you like
                                to purchase? Please enter the
                                number associated with the type
                                of tires:
                                
                                1) Auto Tires
                                2) Truck Tires
                                
                                Enter your selection: """))
                        else:
                            print(f"""
                                There are only {truck_tires} Truck Tires left in inventory.
                                We will contact you when we have replenished our
                                Truck Tires inventory.

                                Sorry for any inconvenience!
                                """)
else:
    print("You did not select an available option.")
