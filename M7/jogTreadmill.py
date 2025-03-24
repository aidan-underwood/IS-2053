# File: jogTreadmill.py
#
# Purpose: To see how to use create lists and how 
#          to manipulate them using various
#          functions and methods in Python.  Lists
#          are created to see how many total miles
#          are jogged on a treadmill and the 
#          average for that week.
#
# Programmer: Aidan Underwood

def main():
    # declare variables to be used in program
    totalMiles = 0.0
    

    # using lists set up the miles jogged
    # for three days and the actual days
    # jogged, respectively
    milesJogged = [0.0, 0.0, 0.0]
    daysJogged = ['Tuesday', 'Thursday', 'Saturday']
    

    # obtain the size of the list 'daysJogged'
    # and print it
    sizeList = len(milesJogged)
    print("milesJogged is of size:", sizeList, "\n")
    

    # using a for loop, prompt the user to enter
    # the amount of miles jogged for each day
    # of the week
    for num in range(sizeList):
        milesJogged[num] = float(input("Enter the amount of miles jogged: "))
    # end for loop


    # using a for loop, calculate a running
    # total for the amount of miles jogged
    for number in milesJogged:
        totalMiles += number
    # end for loop
        
    
    # calculate the average amount of miles
    # jogged per day
    avg = totalMiles / sizeList
    
    # print out lists
    print("\nlist daysJogged: ", daysJogged)
    print("\nlist milesJogged: ", milesJogged)

    # print out the stats
    print("\nTotal amount of miles jogged for the week: ", format(totalMiles, '.2f'))
    print("Average amount of miles jogged per day: ", format(avg, '.2f'))
    
    # call function goodBye() to end program
    goodBye()
# end function main

def goodBye():
    print("\nThis program was written by Aidan Underwood" + "\nEnd of program.")
# end function goodBye


# call/invoke the function main()
main()