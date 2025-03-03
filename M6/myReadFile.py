# File: myReadFile.py
# 
# Purpose: To show how to read from a file in Python.
#
# Programmer: Aidan Underwood

def main():
    # prompt the user to enter the name of the
    # file to be read
    fileName = input("Enter the name of the file to be read: ")
    
    # open the input file
    inputFile = open(fileName, 'r')
    
    # read in from the first and last name of a student
    name = readFile(inputFile)
    # keep reading from file until there is nothing
    # else to be read
    while name != "":
        name = name.rstrip("\n")
        print("name: " + name)
        # read in the amount of credit hours 
        # the user has
        creditHours = readFile(inputFile)
        creditHours = creditHours.rstrip("\n")
        print("creditHours: " + creditHours)
        creditHours = int(creditHours)
        
        # read in the user's message
        message = readFile(inputFile)
        message = message.rstrip("\n")
        print("message: " + message)
        
        # determine what classification the user is
        if creditHours > 0 and creditHours < 30:
            print(name + " is a freshman!\n")
        elif creditHours >= 30 and creditHours < 60:
            print(name + " is a sophomore!\n")
        elif creditHours >= 60 and creditHours < 90:
            print(name + " is a junior!\n")
        elif creditHours >= 90:
            print(name + " is a senior!\n")
        else:
            print("Only undergraduate credit hours are allowed!\n")
        
        # read from file the first and last name
        name = readFile(inputFile)
    # end while loop

    # close the file
    inputFile.close()
    
    # call function goodBye() to end program
    goodBye()   
# end function main

def goodBye():
    print("\nThis program was written by Aidan Underwood" + "\nEnd of program.")
# end function goodBye

def readFile(inputFile):
    item = inputFile.readline()
    return item
# end function readFile

# call/invoke the function main()
main()