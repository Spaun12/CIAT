# Week2 Hands On Exercise PE8 Michael Connell
# Get the cost of the meal
cost_of_meal = float(input("Enter the cost of the meal: "))

# Calculate the tip and the tax
tip = round(cost_of_meal * 0.18, 2)
tax = round(cost_of_meal * 0.07, 2)

# Calculate the total cost of the meal
total_cost = cost_of_meal + tip + tax

# Print the results
print("Tip: ${:.2f}".format(tip))
print("Tax: ${:.2f}".format(tax))
print("Total: ${:.2f}".format(total_cost))
