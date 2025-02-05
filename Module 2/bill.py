# File: bill.py
# 
# Purpose: To calculate the tax, tip, and overall cost of a 
#          meal based upon the user's input of the meal cost.
#
# Programmer: Aidan Underwood


# declare constants to be used
TAX_RATE = 0.07
TIP_RATE = 0.18

# prompt the user for the meal cost, then read it in
bill = float(input("Enter the bill for your meal: "))

# calculate the tax
tax = bill * TAX_RATE

# add the tax to the bill
bill = bill + tax

# now calculate the tip that you would leave
tip = bill * TIP_RATE

# add up the overall total for your meal
totalBill = bill + tip

# print out the results
print("\nTax: $",format(tax, ',.2f'))
print("Tip: $", format(tip, ',.2f'))
print("Total for your meal is: $", format(totalBill, ',.2f'), "\n")

# print message to end program
print("This program was written by Aidan Underwood." + "\nEnd of program.")
