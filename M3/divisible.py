# File: divisible.py
# 
# Purpose: Will determine if the user's input (an
#          integer) is divisible by both 5 and 6 or
#          will determine if the user's input is
#          divisible by 5 or 6 (but not both), or it
#          is not divisible by either one.
#
# Programmer: Aidan Underwood

# prompt the user to enter an integer number, then
# read it in
number = int(input("Enter an integer: "))

# determine which way the user's number is divisible
# by 5 or 6 if at all
if number % 5 == 0 and number % 6 == 0:
    print("The number",number,"is divisible by both 5 and 6.")
elif number % 5 == 0 or number % 6 == 0:
    print("The number",number,"is divisible by either 5 or 6.")
else:
    print("The number",number,"is not divisible by either 5 or 6.")

# print message to end program
print("\nThis program was written by Aidan Underwood." + "\nEnd of program.")
