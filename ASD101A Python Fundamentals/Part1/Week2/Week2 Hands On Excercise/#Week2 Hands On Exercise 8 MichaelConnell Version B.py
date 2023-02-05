#Week2 Hands On Exercise Q8 MichaelConnell

food_charge = float(input("Enter the total cost of the meal: ")) #input the cost of the meal

tip = 0.18 #18% tip adjustable
sales_tax = 0.07 #7% sales tax usually static but sales tax can be changed
# just happend in Kansas this past year

total = ((food_charge * tip) + (food_charge * sales_tax) + food_charge)
#My original approach was much different before the Live session
print(f"""
Your food cost is ${food_charge:,.2f}
You provided a {tip * 100:.0f}% tip
and Sales tax of {sales_tax * 100:.0f}%
Which brings your grand total to ${total:,.2f}.""")
