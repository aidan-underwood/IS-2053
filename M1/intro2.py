# File: intro2.py
# 
# Purpose: To continue to introduce some more basic
#          features of Python.
#
# Programmer: Aidan Underwood


# prompt the user to enter their major, then
# read it in and print it
userMajor = str(input("What is your major?: "))
print()
print("Your major is",userMajor)
# prompt the user to enter how many years they
# have been at UTSA, then read it in and print it
print()
userYears = input("How many years have you been at UTSA?: ")
print()
print("You have been here for " + userYears + " year(s)")
# prompt the user to enter how many coins they have,
# then read it in and print it
print()
userCoins = int(input("How many coins do you have?: "))
print()
print("I have " + str(userCoins) + " coins.")
# add 2 more coins to the current value
# print it
userCoins += 2
print()
print("(add): I stumbled across 2 more coins! I now have " + str(userCoins) + " coins.")

# set up for calculations
number = 4
oddNumber = 3
print()
print("number has the value",number)
print("oddNumber has the value",oddNumber)
# use subtract, multiply, divide, modula,
# and exponent for variable 'coins'
userCoins -= number
print()
print("(subract): I now have",userCoins,"coins.")

userCoins *= number
print()
print("(multiply): I now have",userCoins,"coins.")

userCoins /= oddNumber
print()
print("(float divide): I now have",userCoins,"coins.")

userCoins //= oddNumber
print()
print("(int divide): I now have",userCoins,"coins.")

userCoins %= number
print()
print("(modulo): I have now",userCoins,"coins.")

userCoins **= number
print()
print("(exponent): I now have",userCoins,"coins.")
# how a line continuation characters works
number = number + number * number \
    + oddNumber
print()
print("number new value is",number)
# print message to end program
print()
print("This program was written by Aidan Underwood.")
print("End of program.")