# File: sumPositive.py
# 
# Purpose: Adds up all positive floating-point
#          numbers entered by the user.  A while
#          loop is used to accomplished this.  Adding
#          stops once the user has entered a negative
#          number.  Calculate the average of these
#          numbers.  Final value is then printed out.
#
# Programmer: Aidan Underwood


# set up accumulator variables to hold the summation
# of positive numbers and total number of numbers
# entered
total = 0.0
count = 0

# prompt the user to enter a floating-point
# number, then read it in
number = float(input("Enter a floating-point number (negative to quit): "))

# using a while loop, add up all positive
# numbers entered by the user until a negative 
# number is entered
while (number > 0):
    
    # increase value of how many positive
    # numbers the user has entered
    count += 1
    
    # add value of 'number' to 'total' only 
    # if it is positive
    if number > 0:
        total = total + number
        
    # prompt the user to enter a floating-point
    # number, then read it in
    number = float(input("Enter a floating-point number (negative to quit): "))
# end while loop

# calculate average
if count != 0:
    average = total / count
else:
    average = 0.0
# display the results
print("\nFinal value of positive numbers: ", format(total, ',.2f'))
print("Average was: ", format(average, ',.2f'))
print("There were",count,"numbers entered.")
# print message to end program
print("\nThis program was written by Aidan Underwood" + "\nEnd of program.")