#Hourly Pay Coding bones

def calculate_pay(hours_worked, pay_rate):
    normal_pay = 0
    time_and_a_half_pay = 0
    double_time_pay = 0

    # Check if hours worked is less than or equal to 40
    if hours_worked <= 40:
        # If yes, then calculate pay by multiplying hours worked with pay rate
        normal_pay = hours_worked * pay_rate
        gross_pay = normal_pay

    # Check if hours worked is less than or equal to 50
    elif hours_worked <= 50:
        # If yes, then calculate pay for first 40 hours and overtime pay for remaining hours
        normal_pay = 40 * pay_rate
        time_and_a_half_pay = (hours_worked - 40) * (pay_rate * 1.5)
        gross_pay = normal_pay + time_and_a_half_pay

    # Check if hours worked is less than or equal to 80
    elif hours_worked <= 80:
        # If yes, then calculate pay for first 40 hours, overtime pay for next 10 hours, and double time pay for remaining hours
        normal_pay = 40 * pay_rate
        time_and_a_half_pay = (pay_rate * (1.5 * 10)) 
        double_time_pay = (hours_worked - 50) * (pay_rate * 2)
        gross_pay = normal_pay + time_and_a_half_pay + double_time_pay
    else:
        # If hours worked is above 80, then print error message
        print("Error: cannot enter hours above 80.")
        return
    # Return the calculated gross pay and the normal, time and a half and double time pay
    return gross_pay, normal_pay, time_and_a_half_pay, double_time_pay

while True:
    # Get input for hours worked
    hours_worked = int(input("Enter hours worked: "))
    # Check if hours worked is above 80
    if hours_worked > 80:
        print("Error: cannot enter hours above 80.")
        continue
    break
while True:
    # Get input for pay rate
    pay_rate = float(input("Enter pay rate: "))
    # Check if pay rate is negative
    if pay_rate < 0:
        print("Error: pay rate cannot be negative.")
        continue
    break

# Call the calculate_pay function to get the gross pay
gross_pay, normal_pay, time_and_a_half_pay, double_time_pay = calculate_pay(hours_worked, pay_rate)

# Format gross pay, normal_pay, time_and_a_half_pay, double_time_pay to display with 2 decimal places
gross_pay_formatted = "{:.2f}".format(gross_pay)
normal_pay_formatted = "{:.2f}".format(normal_pay)
time_and_a_half_pay_formatted = "{:.2f}".format(time_and_a_half_pay)
double_time_pay_formatted = "{:.2f}".format(double_time_pay)

# Print the gross pay, normal_pay, time_and
print("Normal pay: $" + str(normal_pay_formatted))
print("Time and a half pay: $" + str(time_and_a_half_pay_formatted))
print("Double time pay: $" + str(double_time_pay_formatted))
print("Gross pay: $" + str(gross_pay_formatted))


