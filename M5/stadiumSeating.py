# File: stadiumSeating.py
# 
# Purpose: Calculates the total income generated for a stadium
#          based upon the number of tickets sold.  Different
#          class tickets can be sold with different prices.
#          Calculate each income for each class ticket as 
#          well as the overall income and print out these
#          statistics.
#
# Programmer: Aidan Underwood

# declare global constants to be used in program
CLASS_A_SEATS = 20.00
CLASS_B_SEATS = 15.00
CLASS_C_SEATS = 10.00

def main():
    # prompt the user to enter the amount of 
    # A seats, then read it in
    countAseats = int(input("Enter count of A seats: "))
    # prompt the user to enter the amount of 
    # B seats, then read it in
    countBseats = int(input("Enter count of B seats: "))
    # prompt the user to enter the amount of 
    # C seats, then read it in
    countCseats = int(input("Enter count of C seats: "))
    
    # calculate the A income
    incomeAseats = countAseats * CLASS_A_SEATS
    # calculate the B income
    incomeBseats = countBseats * CLASS_B_SEATS
    # calculate the C income
    incomeCseats = countCseats * CLASS_C_SEATS

    # call function calcIncome() to sum up the total
    # income for all tickets
    total = calcIncome(incomeAseats, incomeBseats, incomeCseats)
    
    # call function displayIncome() to print out statistics
    displayIncome(incomeAseats, incomeBseats, incomeCseats, total)
    
    # call function goodBye() to end program    
    goodBye()
# end function main

def goodBye():
    print("\nThis program was written by Aidan Underwood" + "\nEnd of program.")
# end function goodBye

def displayIncome(incomeA, incomeB, incomeC, totalIncome):
    # display results
    print("\nIncome from class A seats is $", format(incomeA, ",.2f"))
    print("Income from class B seats is $", format(incomeB, ",.2f"))
    print("Income from class C seats is $", format(incomeC, ",.2f"))
    print("Total income for stadium: $", format(totalIncome, ",.2f"))
# end function displayIncome

def calcIncome(incomeA, incomeB, incomeC):
    # calculate the total income
    totalIncome = incomeA + incomeB + incomeC
    # return the total income
    return totalIncome
# end function calcIncome

# call/invoke the function main()
main()