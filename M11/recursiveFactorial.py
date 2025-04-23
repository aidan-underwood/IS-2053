# File: recursiveFactorial.py
#
# Purpose: To recursively calculate the factorial of
#          a number that is entered by the user.
#
# Programmer: Aidan Underwood

def main():
    # prompt the user to enter an integer that is at
    # least 0 in value, then read it in
    num = int(input("Please enter an integer (or -1 to quit): "))
    print("You entered", num, "for recursion")

    # using a while loop, calculate the
    # factorial of ‘num’ until user enters -1
    while num >= 0:  # or num != -1
        theFact = factorial(num)
        print("The factorial of", num, "! is", theFact)
        num = int(input("\nPlease enter an integer (or -1 to quit): "))

    # call function goodBye() to end program
    goodBye()

# end function main

def factorial(n):
    if n == 0:  # base case
        print("Reached the base case. Returning 1")
        return 1
    else:  # recursive case
        answer = n * factorial(n - 1)
        print("Processing the following:", n, "*", n - 1, "!, ->", answer)
        return answer
# end function factorial

def goodBye():
    print("\nThis program was written by Aidan Underwood" + "\nEnd of program.")
# end function goodBye

# call/invoke the function main()
main()