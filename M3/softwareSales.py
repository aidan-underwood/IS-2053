# File: softwareSales.py
# 
# Purpose: To calculate the final amount of purchase
#          based upon the user's input of packages
#          purchased and any applied discount.
#          First solve this with logcial operators
#          and then solve it without logical 
#          operators.
#
# Programmer: Aidan Underwood


# declare constant to be used in program
RETAIL_PRICE = 99.00

# prompt the user to enter how many packages they
# have purchased, then read it in
quantity = int(input("Enter the number of packages purchased: "))

# calculate the discount rate using
# logical operators

#if (quantity >= 10 and quantity <= 19):
#    discountRate = 0.10
#elif (quantity >= 20 and quantity <= 49):
#    discountRate = 0.20
#elif (quantity >= 50 and quantity <= 99):
#    discountRate = 0.30
#elif (quantity >= 100):
#    discountRate = 0.40
#else:
#    discountRate = 0.0

# calculate again the discount rate but without
# using logical operators
if quantity < 9:
    discountRate = 0.0
elif quantity < 19:   
    discountRate = 0.10
elif quantity < 49:   
    discountRate = 0.20
elif quantity < 99:  
    discountRate = 0.30
else:                
    discountRate = 0.40

# calculate the full price
fullPrice = quantity * RETAIL_PRICE

# calculate the discount amount
discountAmount = fullPrice * discountRate

# calculate the total amount (i.e., take
# off the discount from the full price)
finalAmount = fullPrice - discountAmount

# print out the results
print("\nFull amount (before discount): $", format(fullPrice, ',.2f'))
print("Discount amount: $", format(discountAmount, ',.2f'))
print("Final amount: $", format(finalAmount, ',.2f'))

# print message to end program
print("\nThis program was written by Aidan Underwood" + "\nEnd of program.")