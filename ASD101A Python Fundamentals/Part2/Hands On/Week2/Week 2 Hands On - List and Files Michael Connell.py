# Week 2 Hands On - List and Files Michael Connell
import matplotlib.pyplot as plt
# Initialize an empty list to store the sales for each day of the week
sales = []
# Use a loop to ask the user to enter the sales for each day of the week
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
for day in days:
    while True:
        try:
            sale = float(input(f"Enter sales for {day}: "))
            if sale < 0:
                raise ValueError("Sales cannot be negative")
            sales.append(sale)
            break
        except ValueError as e:
            print(f"Invalid input: {e}")
# Calculate the total sales for the week
total_sales = sum(sales)
# Display the total sales for the week
print(f"Total sales for the week: ${total_sales:.2f}")
# Plot the sales for each day of the week in a bar chart
plt.bar(days, sales)
plt.title("Sales for the Week")
plt.xlabel("Day")
plt.ylabel("Sales")
plt.show()