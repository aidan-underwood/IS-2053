# File: countNumbers.py
# 
# Purpose: To calculate various statistics on integer 
#          numbers that will be entered by the user.
#          Number of positive and negative numbers as
#          well as the total value and average of these
#          numbers are calculated and then displayed.
#
# Programmer: Aidan Underwood

# intialize variables appropriately for counting
countPositive = 0
countNegative = 0
total = 0
count = 0

# prompt the user to enter an integer number, then
# read it in
num = int(input("Enter an integer number, enter 0 to quit: "))

# using a while loop, keep track of  how many positive
# and negative numbers we have seen.  Once the sentinel
# value of zero has been entered, fall out of the while
# loop
while num != 0:
    if num > 0:
        countPositive += 1
    else:
        countNegative += 1
    # tally up running total and how
    # many numbers we have seen
    total += num
    count += 1
    
    # prompt the user to enter an integer number, then
    # read it in
    num = int(input("Enter an integer number, enter 0 to quit: "))
# end while loop

if count == 0:
    print("No numbers were entered except 0")
else:
    average = total / count
    print("\nNumber of positives was", countPositive)
    print("Number of negatives was", countNegative)
    print("The total was", total)
    print("The average was", format(average, ",.2f"))

# print out statistics

# print message to end program
print("\nThis program was written by Aidan Underwood" + "\nEnd of program.")