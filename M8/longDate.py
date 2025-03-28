# File: longDate.py
# 
# Purpose: To read in a date from the user in the
#          format mm/dd/yyyy and then convert it
#          to long date format.
#
# Programmer: Aidan Underwood

def main():
    # create a tuple consisting of the months
    monthName = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
    
    # prompt the user to enter a date in the
    # format mm/dd/yyyy, then read it in
    userDate = input("Please enter a date in the format mm/dd/yyyy: ")

    # split up the 'userDate' so that a list
    # is created consisting of the components
    # of the date the user entered
    dateList = userDate.split("/")
    
    # print out 'dateList'
    print("\nHere is dateList: ")
    print(dateList)
    
    # extract out the numbered month, day,
    # and the year
    monthNum = int(dateList[0])
    dayNum = int(dateList[1])
    year = dateList[2]
    
    dayStr = str(dayNum)

    # using 'monthNum' obtain the actual name
    # of the month from the tuple 'monthName'
    monthStr = monthName[monthNum - 1]

    # build a string in long date format
    # conisting of the monthStr, day, and year
    longDate = monthStr + " " + dayStr + ", " + year
    
    # print out 'longDate' (i.e., long date format)
    print("\nHere is the long date format: ")
    print(longDate)
    
    # call function goodBye() to end program
    goodBye()
# end function main


def goodBye():
    print("\nThis program was written by Aidan Underwood" + "\nEnd of program.")
# end function goodBye

# call/invoke the function main()
main()