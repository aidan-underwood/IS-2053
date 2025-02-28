# File: myWriteFile.py
# 
# Purpose: To show how to write to a file in Python.
#
# Programmer: Aidan Underwood

def main():
    # prompt the user to enter the name of the file,
    # then read it
    fileName = input("Enter the name of the file to which results will be written: ")
    # open output file
    outputFile = open(fileName, 'w')
    keepLooping = True
    # keep looping until the user no longer
    # wishes to continue
    while keepLooping:
    
        # prompt the user to enter a first name
        # then read it in;  then repeat for last
        # name
        firstName = input("Enter a first name: ")
        lastName = input("Enter a last name: ")
        # prompt the user to enter their 
        # credit hours, then read it in
        creditHours = int(input("Enter the number of credit hours: "))
        # write to the file the first and last
        # name of student
        writeFile(outputFile, firstName + " ")
        writeFile(outputFile, lastName + "\n") 
        # write to file the credit hours
        writeFile(outputFile, str(creditHours) + "\n")
        
        invalidChoice = True
        # keep looping until valid
        # degree is chose        
        while invalidChoice:
            # obtain the user's choice
            print("\nWhat is the highest degree that they want to obtain?")
            print("1 - Bachelor's")
            print("2 - Master's")
            print("3 - Doctoral")
            choice = int(input())
            # depending on whether has chosen a bachelor's,
            # master's, or doctoral degree call function
            # writeFile(), to write appropriate message
            # to that file
            if choice == 1 or choice == 2 or choice == 3:
                if choice == 1:
                    print("Go and get that bachelor's degree now!")
                    writeFile(outputFile, "Cannot wait to starting working can you " + firstName + "?\n")
                elif choice == 2:
                    print("Good decision that you are going after that Master's degree!")
                    writeFile(outputFile, "So will I have to call you Master " + firstName + " " + lastName + "?\n")
                else:
                    print("Going for the top degree I see-Doctoral!")
                    writeFile(outputFile, "How does Dr. " + firstName + " " + lastName + " sound?\n")
                invalidChoice = False
            else:
                print("Invalid choice.  Please try again.")
        # end inner while loop
        
        # prompt the user if they wish to
        # continue, then read it in
        answer = input("Do you wish to continue? (y/n): ")
        if answer == 'n' or answer == 'N':
            keepLooping = False
    # end outer while loop

    # call function goodBye() to end program
    goodBye()
    # close the file
    outputFile.close()
# end function main

def goodBye():
    print("\nThis program was written by Aidan Underwood" + "\nEnd of program.")
# end function goodBye

def writeFile(toFile, message):
    toFile.write(message)
# end function writeFile


# call/invoke the function main()
main()