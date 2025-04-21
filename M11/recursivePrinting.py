# File: recursivePrinting.py
# 
# Purpose: To create a function that will accept one integer
#          paramater ('num') and have it recursively print
#          out the numbers from 1 through 'num' one number
#          per line.
# 
# Programmer: Aidan Underwood

def main():
    # prompt the user to enter an integer number
    # then read it in
    n = int(input("Please enter an integer number: "))

    # call the function 'printNum()' to print out
    # the numbers 1 through 'n'
    printNum(n)
        
    # call function goodBye() to end program
    goodBye()


# end function main

def printNum(num):
    if num == 1: # base case
        print(num)
    else: # recursive case
        printNum(num - 1)
        print(num)
# end function printNum

def goodBye():
    print("\nThis program was written by Aidan Underwood" + "\nEnd of program.")
# end function goodBye

# call/invoke the function main()
main()