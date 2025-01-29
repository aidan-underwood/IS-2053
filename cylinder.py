# File: cylinder.py
# 
# Purpose: To computer the volume of a cylinder.
#
# Programmer: 


# declare a constant for PI
pi = 3.14159
# prompt the user for the radius and the length of a
# cylinder, then read them in
radius = float(input("What is the radius of your cylinder? "))
length = float(input("What is the length of your cylinder? "))
# calculate the volume of a cylinder
volume = radius**2 * pi * length
# print out the results
print(volume)
# print message to end program
print("This program was written by Aidan Underwood.")
print("End of program.")
