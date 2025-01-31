# File: acres.py
# 
# Purpose: To calculate the amount of acres of land based
#          upon the user's input of square feet.
#
# Programmer: Aidan Underwood


# declare constant to be used in program
sqFeet = 43560

# prompt the user for amount of square feet (integer),
# then read it in
userFeet = int(input("Input the amount of square feet: "))

# calculate the amount of acres
acres = userFeet / sqFeet

# print out the results
print("This is equivalent to", format(acres, ".4f"),"acres.")

# print message to end program
print("This program was written by Aidan Underwood.")
print("End of program.")