# File: initials.py
# 
# Purpose: To read in a user's full name and create
#          the initials based upon their name.
#
# Programmer: Aidan Underwood

def main():
    # prompt the user to enter their first name,
    # middle name, and their last name, 
    # then read them all in
    fullName = input("Please enter your full name (first, middle, last): ")

    # split up the 'fullName' so that a list
    # is created consisting of the components
    # of the user's entire name
    nameList = fullName.split(" ")
    
    # print out 'nameList'
    print("\nHere is nameList: ", nameList)
    
    # go through 'nameList' and extract out the
    # first character of each item in the list
    # to make it an initial that will be 
    # followed by a period and a space
    for string in nameList:
        print(string[0].upper(), end=". ")
    
    # call function goodBye() to end program
    goodBye()
# end function main

def goodBye():
    print("\n\nThis program was written by Aidan Underwood" + "\nEnd of program.")
# end function goodBye

# call/invoke the function main()
main()