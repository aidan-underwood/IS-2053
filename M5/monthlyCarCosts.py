# File: monthlyCarCosts.py
# 
# Purpose: Calculates the monthly and yearly car costs
#          for a user by prompting the user for various
#          costs for their car.  A function is used
#          to calculate these statistics and then
#          print them out.
#
# Programmer: Aidan Underwood

def main():
    # prompt the user to enter various monthly 
    # costs for their car (loan, insurance, gas,
    # oil, tires, general monthly maintenance), then
    # read them in, respectively
    loan = float(input("Enter the monthly loan amount: "))
    insurance = float(input("Enter the monthly insurance amount: "))
    gas = float(input("Enter the monthly gas amount: "))
    oil = float(input("Enter the monthly oil amount: "))
    tires = float(input("Enter the monthly tire amount: "))
    maintenance = float(input("Enter the monthly maintenance amount: "))
    
    # call function showExpenses() to calculate the
    # monthly and yearly car costs which are then
    # printed out
    showExpenses(loan, insurance, gas, oil, tires, maintenance)
        
    # call function goodBye() to end program
    goodBye()
# end function main

def showExpenses(loan, insurance, gas, oil, tires, maintenance):
    totalMonth = loan + insurance + gas + oil + tires + maintenance
    totalYear = totalMonth * 12
    
    print("\nTotal monthly expense: $", format(totalMonth, ",.2f"))
    print("Total annual expense: $", format(totalYear, ",.2f"))
# end function showExpenses
        
def goodBye():
    print("\nThis program was written by Aidan Underwood" + "\nEnd of program.")
# end function goodBye

# call/invoke the function main()
main()