# File: salesTax.py
# 
# Purpose: To calculate the subtotal, sales tax, and
#          the overall total for the amount of prices
#          (float) of items that are entered by the user.
#
# Programmer: Aidan Underwood


# declare constant to be used in program
TAX_RATE = 0.07

# prompt the user for the prices (float) of each item,
# then read them in
item1 = float(input("Enter the price (float) of item #1: "))
item2 = float(input("Enter the price (float) of item #2: "))
item3 = float(input("Enter the price (float) of item #3: "))
item4 = float(input("Enter the price (float) of item #4: "))
item5 = float(input("Enter the price (float) of item #5: "))

# calculate the subtotal
subtotal = item1 + item2 + item3 + item4 + item5

# calculate the sales tax 
salesTax = subtotal * TAX_RATE

# calculate the total
total = subtotal + salesTax

# print out the results
print("\nSubtotal: $", format(subtotal, ',.2f'))
print("Sales tax: $", format(salesTax, ',.2f'))
print("Total: $", format(total, ',.2f'))

# print message to end program
print("\nThis program was written by Aidan Underwood")
print("End of program.")