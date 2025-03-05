# File: writeReadFile.py
# 
# Purpose: To randomly generate a specific amount of 
#          integer numbers and write them to a file.
#          Then read them from a file and sum up the
#          numbers as well as their average.  Also, a
#          look at how to handle exceptions.
#
# Programmer: Aidan Underwood

import random

def main():
    # zero out accumulator variables
    total = 0
    counter = 0
    
    # prompt the user for the file name,
    # then read it in
    fileName = input("Please enter the file name: ")
    print("File name is: " + fileName)
    
    # prompt the user to enter how many random
    # integer numbers they wish to have and also
    # the upper bound range for these numbers  
    maxNum = int(input("How many random integer numbers do you want? "))
    upperBound = int(input("What is the upper bound for number range? "))
    
    # open a file to write to
    outFile = open(fileName, 'w')
    
    # using a for loop randomly generate 'maxNum'
    # numbers and write them to a file
    for i in range(0, maxNum):
        num = random.randrange(1, upperBound + 1)
        outFile.write(str(num) + "\n")
    # end for loop
    
    # close the file
    outFile.close()
    
    # now open the file for reading purposes
    inFile = open(fileName, 'r')
    
    # read the data (the numbers) from the file;
    # keep track of how many numbers there are 
    # as well as a running total;  this for
    # loop will read from the file until no
    # more records to be read
    for line in inFile:
        num = int(line)
        counter += 1
        total += num
    # end for loop
    
    # close the file 
    inFile.close()
    
    # calculate the average of the numbers
    # that were read from the file
    average = total / counter
    
    # print out statistics about the numbers
    print("\nThere were " + str(counter) + " numbers.")
    print("Total sum for numbers is: " + str(total))
    print("Average: ", format(average, ',.2f'))
    
    # create a false file name
    fileName2 = "aidan.txt"
    
    # create an exception that will catch an
    # invalid file name that was to be read from  
    try:
        inFile2 = open(fileName2, 'r')
    except IOError:
        print("\nError: File not found.")
        
    # create an exeption that will catch an 
    # invalid division by zero; otherwise print
    # out an acceptable message that the division
    # was okay
    try:
        num = random.randrange(0,3)
        average = total / num
    except ZeroDivisionError:
        print("\nError: Cannot divide by zero.")
    else:
        print("\nDividing by",num,"was acceptable.")

    # call goodBye() to end program
    goodBye()
# end function main

def goodBye():
    print("\nThis program was written by Aidan Underwood" + "\nEnd of program.")
# end function goodBye

# call/invoke the function main()
main()