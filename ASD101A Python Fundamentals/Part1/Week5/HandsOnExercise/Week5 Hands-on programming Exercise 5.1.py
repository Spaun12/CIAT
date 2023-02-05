#Week5 Hands-on programming Exercise 5.1
# This function prompts the user to enter a distance
def get_distance():
    distance = input("Enter a distance: ")
    return float(distance)

# This function prompts the user to enter the unit of the distance
def get_unit():
    unit = input("Enter the unit of the distance (km or mi): ").lower()
    return unit

# This function converts kilometers to miles using the conversion formula
def km_to_miles(distance_km):
    miles = distance_km * 0.621371
    return round(miles, 2)
    
#This function converts miles to kilometers using the conversion formula
def miles_to_km(distance_mi):
    kilometers = distance_mi * 1.60934
    return round(kilometers, 2)
    
# Main program
while True:
    unit = get_unit()
    distance = get_distance()
    if unit == "km":
        distance_miles = km_to_miles(distance)
        print("Distance in miles: ", distance_miles)
    elif unit == "mi":
        distance_km = miles_to_km(distance)
        print("Distance in kilometers: ", distance_km)
    else:
        print("Invalid unit entered, please enter either 'km' or 'mi'")
    again = input("Do you want to enter another value? (yes or no): ").lower()
    if again != "yes":
        break
