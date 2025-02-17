# File: days.py
# 
# Purpose: Based upon the user's input (an integer) display
#          the appropriate day of the week.  Also, based
#          upon the user's second input (an integer)
#          display the future day by adding the number of
#          days (second integer) to the first integer
#
# Programmer: Aidan Underwood


# prompt the user to enter an integer number, 
# then read it in
today = int(input("Enter today's days: "))

# determine the appropriate day based upon the 
# user's input
if today == 0:
    nameForToday = "Sunday"
elif today == 1:
    nameForToday = "Monday"
elif today == 2:
    nameForToday = "Tuesday"
elif today == 3:
    nameForToday = "Wednesday"
elif today == 4:
    nameForToday = "Thursday"
elif today == 5:
    nameForToday = "Friday"
elif today == 6:
    nameForToday = "Saturday"
else:
    nameForToday = "defaulted to Sunday"
    today = 0
# print out the day
print("Today is",nameForToday)

# prompt the user to enter another integer
# number, then read it in
elapsedDays = int(input("Enter the number of days elapsed since today: "))

# determine the appropriate future day 
# based upon the user's input
futureDay = (today + elapsedDays) % 7


# determine the appropriate future day based upon
# the user's input
if futureDay == 0:
    nameForFutureDay = "Sunday"
elif futureDay == 1:
    nameForFutureDay = "Monday"
elif futureDay == 2:
    nameForFutureDay = "Tuesday"
elif futureDay == 3:
    nameForFutureDay = "Wednesday"
elif futureDay == 4:
    nameForFutureDay = "Thursday"
elif futureDay == 5:
    nameForFutureDay = "Friday"
elif futureDay == 6:
    nameForFutureDay = "Saturday"
else:
    nameForFutureDay = "Unknown day"
    futureDay = 0

# print out the future day
print("The future will be", nameForFutureDay)

# print message to end program
print("\nThis program was written by Aidan Underwood." + "\nEnd of program.")