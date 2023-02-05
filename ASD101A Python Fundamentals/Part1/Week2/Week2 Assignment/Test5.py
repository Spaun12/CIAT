food_charge = float(input('enter the foods orginal price:'))

tax = (7/100) * food_charge
sales_tax = float(tax)
tip = (18/100) * food_charge
meal_cost = food_charge + tax + tip

print(f''' Food cost: {food_charge} 
tax: {tax:,.2f}%
tip: {tip:,.2f}%
total cost: ${meal_cost:,.2f} ''')