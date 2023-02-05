#week2 Hands On Exercise 8 MichaelConnell Response version c

while True:
    try:
        food_charge = float(input("Enter the total cost of the meal: ")) #input the cost of the meal
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

tip_percentage = float(input("Enter the tip percentage (e.g. 18 for 18%): "))
tip = tip_percentage / 100

sales_tax_percentage = float(input("Enter the sales tax percentage (e.g. 7 for 7%): "))
sales_tax = sales_tax_percentage / 100

tip_amount = food_charge * tip
tax_amount = food_charge * sales_tax
total = food_charge + tip_amount + tax_amount

print(f"""
Food Charge : ${food_charge:,.2f}
Tip         : {tip_percentage:,.0f}%
Sales Tax   : {sales_tax_percentage:,.1f}%

Grand Total : ${total:,.2f}""")
