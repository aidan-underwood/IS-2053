# File: splitdigits.py
# 
# Purpose: To see how to print each digit of a 4 digit number
#          on a separate line.
#
# Programmer: Aidan Underwood


# prompt the user to enter a 4 digit number, then
# read it in
number = int(input("Enter an integer (4 digits): "))
# extract out the last number (4th), then truncate the
# number by removing the 4th number
d4 = number % 10
number = number // 10

# extract out the last number (3rd), then truncate the
# number by removing the 3rd number
d3 = number % 10
number = number // 10

# extract out the last number (2nd), then truncate the
# number by removing the 2nd number
d2 = number % 10
number = number // 10

# extract out the last number (1st), then truncate the
# number by removing the 1st number
d1 = number % 10
number = number // 10

# print out each digit on a separate line
print(d1)
print(d2)
print(d3)
print(d4)

# print message to end program
print("\nThis program was written by Aidan Underwood" + "\nEnd of program.")
