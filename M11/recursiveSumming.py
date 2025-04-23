# File: recursiveSumming.py
#
# Purpose: To create a function that will accept one integer
#          parameter ('num') and have it recursively sum up
#          the numbers 1 through 'num' (where the value of
#          'num' will be entered by the user and will
#          originally be called 'n').  Also, sum up the
#          numbers in an iterative fashion using a for
#          loop to compare this value with the recursive
#          value.
# 
# Programmer: Aidan Underwood

def main():
    # initialize variable so it may accummulate
    # the numbers
    iterativeSum = 0
    
    # prompt the user to enter an integer value that is 
    # at least 1 in value, then read it in and sum it up
    n = int(input("Please enter an integer (1 or higher): "))
    print("\nWill be adding numbers from 1 through", n, "\n")
    
    # add up the numbers in an iterative way
    # using a for loop
    for count in range(1, n + 1):
        iterativeSum += count
    # end for loop
    
    # print out the sum via iterative way
    print("Iterative sum:", iterativeSum)
    
    # call the function 'sumNums()'
    recursiveSum = sumNums(n)
    
    # print out the sum via recursive way
    print("Recursive sum:", recursiveSum)
    
    # call function goodBye() to end program
    goodBye()
# end main function

def sumNums(num):
    if num == 1: # base case
        return num
    else: # recursive case
        return num + sumNums(num - 1)
# end function sumNums

def goodBye():
    print("\nThis program was written by Aidan Underwood" + "\nEnd of program.")
# end goodBye function

# call/invoke the function main()
main()