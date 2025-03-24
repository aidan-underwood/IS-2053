# File: greaterThanN.py
#
# Purpose: To see which numbers within a list are 
#          greater in value than the value of
#          the number that the user has entered
#          from the keyboard.  The function
#          'greaterList()' will determine this
#          outcome.
#
# Programmer: Aidan Underwood

def main():
    # declare variables and lists to be
    # used in program
    numbers = [21, 4, 19, 6, 11, 40, 7, 37, 2, 15]
    
    # print out the list
    print("list numbers: ", numbers, "\n")
    
    # prompt the user to enter an integer
    # number, then read it in
    userNum = int(input("Enter an integer number: "))
    
    # display the list of numbers that are larger
    # than 'choice'
    print("\nNumbers in list that are greater than", userNum)
    
    # call function 'greaterList()' to determine
    # what numbers are greater than the value 
    # of 'choice' 
    greaterList(userNum, numbers)
    
    # call function goodBye() to end program
    goodBye()
# end function main


def greaterList(n, originalList):
    newList = []
    for aNum in originalList:
        if aNum > n:
            newList.append(aNum)
    print(newList)
# end function greaterList

def goodBye():
    print("\nThis program was written by Aidan Underwood" + "\nEnd of program.")
# end function goodBye

# call/invoke the function main()
main()