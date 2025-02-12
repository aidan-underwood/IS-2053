# File: pennyDay.py
# 
# Purpose: To calculate the amount of pay the user
#          will get starting off with a single
#          penny for the first day.  Each day, the
#          current amount will be doubled and will
#          continue until the user's input for
#          amount of days to calculate.
#
# Programmer: Aidan Underwood


# set up accumulator variables that will be the total
# amount of pay that user will get over the amount
# of days
dayPennies = 1
total = 0.0

# prompt the user to enter the number of days
# the user will get paid, then read it in
numDays = int(input("Enter the number of days: "))

# print out a header for a table 
print("\nDay\tPennies")
print("---------------")

# using a for loop print out the user's pay
# for each day as it gets doubled in value
for day in range(1, numDays + 1):
    print(day, "\t$", format(dayPennies / 100, ",.2f"))
    total += dayPennies
    dayPennies *= 2
# end for loop

# display the results
print("\nThe total salary for",numDays,"days is: $", format(total / 100, ",.2f"))
    
# print message to end program
print("\nThis program was written by Aidan Underwood" + "\nEnd of program.")