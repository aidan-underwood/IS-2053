# File: mpg.py
# 
# Purpose: To calculate the mpg that a car gets based upon
#          the amount of miles that has been driven
#          and the amount of gallons of gas used.
#
# Programmer: Aidan Underwood


# prompt the user the enter the amount of miles that
# has been driven, then read it in
miles = int(input("How many miles have you driven?: "))
# prompt the user to enter the amount of gallons of
# gas used, then read it in
gas = float(input("How many gallons of gas did you use?: "))
# calculate the miles per gallon
mpg = miles / gas
# print out the results
print("You got an average MPG of",format(mpg, ".2f"))
# print message to end program
print("This program was written by Aidan Underwood.")
print("End of program.")