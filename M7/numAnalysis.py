# File: numAnalysis.py
#
# Purpose: To see how to use create lists and how 
#          to manipulate them using various
#          functions and methods in Python.  
#          Random integer numbers are created to
#          populate a list and then various
#          statistics are obtained via existing
#          functions.
#
# Programmer: Aidan Underwood

import random

def main():
    # declare constants to be used in program
    NUM = 20
    NUM_RANGE = 1000

    # declare list to be used in program
    allNums = []

    # populate the list 'allNums' with
    # random numbers
    for i in range(NUM):
        number = random.randrange(1, NUM_RANGE + 1)
        allNums.append(number)
    # end for loop
    
    # print the list 'allNums'
    print("list allNums: ", allNums, "\n")

    # calculate stats from the list 'allNums'
    sizeList = len(allNums)
    low = min(allNums)
    high = max(allNums)
    total = sum(allNums)
    avg = total / sizeList
    
    # print out stats
    print("Size of list allNums: ", sizeList)
    print("Lowest number in list allNums: ", low)
    print("Highest number in list allNums: ", high)
    print("Total of numbers in list allNums: ", total)
    print("Average of numbers in list allNums: ", format(avg, ',.2f'))
    
    # call function goodBye() to end program
    goodBye()
# end function main

def goodBye():
    print("\nThis program was written by Aidan Underwood" + "\nEnd of program.")
# end function goodBye

# call/invoke the function main()
main()