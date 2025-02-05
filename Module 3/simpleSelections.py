# File: simpleSelections.py
# 
# Purpose: To see if a person, based upon their age
#          that is entered by the user, is old enough
#          to vote.  Also determines if this person
#          is an infant, a child, a teenager, or
#          an adult.
#
# Programmer: Aidan Underwood


# prompt the user to enter an age (i.e., an integer)
# then read it in
age = int(input("Enter an age: "))

# determine if the user is old enough to vote.
# If so, print out appropriate message.  Otherwise,
# print out appropriate message that they cannot
if age >= 18:
    print("You are old enough to vote!")
    print("Now I know that I am getting older. \n")
else:
    print("Sorry, but you cannot vote!")
    print("Maybe on your next birthday? \n")
    
# determine if the person is an infant, a child, 
# a teenager, or an adult.  Print out appropriate
# message
if age <= 1:
    print("This person is an infant.")
elif age > 1 and age < 13:
    print("This person is a child.")
elif age >= 13 and age < 20:
    print("This person is a teenager.")
else:
    print("This person is an adult.")

# print message to end program
print("\nThis program was writtn by Aidan Underwood" + "\nEnd of program.")
