# File: rainFall.py
# 
# Purpose: A tuple holding the names of the months of
#          the year and a list holding the amount of
#          rainfall for the months are created.  The 
#          amount of rainfall for each month is going
#          to be randomly generated as floating-point
#          numbers.  Various statistics will be printed
#          via a function 'displayResults()'.
#
# Programmer: Aidan Underwood

import random

def main():
    # using a tuple create the months of the year
    monthName = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
    # using a list set up the monthly rainfall
    monthRain = [0.0] * 12
    
    # obtain the size of the list 'monthName'
    sizeList = len(monthName)
    # randomly generate the rainfall  for each month;
    # they will be floating-points numbers between the
    # range of 0.0 and 12.999
    for i in range(sizeList):
        monthRain[i] = random.uniform(0.0, 12.999)
        
    # print out each month's name and its rainfall
    for i in range(sizeList):
        print(monthName[i], ":", format(monthRain[i], ".2f"), "inches")
        
    # obtain the total rainfall for the year
    total = sum(monthRain)
    
    # calculate the average amount of rainfall
    # per month for the year
    average = total / sizeList
    
    # obtain the maximum of monthly rainfall
    # for the year
    maxRain = max(monthRain)
    
    # obtain the index of the month that 
    # has the highest amount of rainfall for
    # the year
    monthHighestIndex = monthRain.index(maxRain)
    
    # obtain the month name that has the highest
    # amount of rainfall for the year
    monthHighestName = monthName[monthHighestIndex]
    
    # obtain the minimum of monthly rainfall
    # for the year
    minRain = min(monthRain)
    
    # obtain the index of the month that
    # has the lowest amount of rainfall for
    # the year
    monthLowestIndex = monthRain.index(minRain)
    
    # obtain the month name that has the lowest
    # amount of rainfall for the year
    monthLowestName = monthName[monthLowestIndex]
    
    # call/invoke the function 'displayResults()' to
    # print out the statistics
    displayResults(total, average, monthHighestName, maxRain, monthLowestName, minRain)

    # call function goodBye() to end program
    goodBye()
# end function main

def displayResults(total, avg, monthMaxName, highestMonthRain, monthMinName, lowestMonthRain):
    print("\nTotal rainfall for the year: ", format(total, ".2f"), "inches")
    print("Average monthly rainfall: ", format(avg, ".2f"), "inches")
    print("Month with the highest amount of rainfall: ", monthMaxName, "with", format(highestMonthRain, ".2f"), "inches")
    print("Month with the lowest amount of rainfall: ", monthMinName, "with", format(lowestMonthRain, ".2f"), "inches")
# end function displayResults

def goodBye():
    print("\nThis program was written by Aidan Underwood" + "\nEnd of program.")
# end function goodBye


# call/invoke the function main()
main()