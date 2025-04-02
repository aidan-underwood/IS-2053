# File: funWithStrings.py
# 
# Purpose: A sentence will be read in and will be scanned
#          character by character to determine whether
#          the given character is uppercase, lowercase,
#          a digit, a space, or a symbol.  Then first and
#          last name of user will be entered and various
#          string operations will be performed on it.  A
#          list  will be constructed from the sentence.
#
# Programmer: Aidan Underwood

def main():
    # declare variables to be used 
    # to accumulate occurrences of 
    # different types of characters
    numUpper = 0
    numLower = 0
    numSpace = 0
    numDigit = 0
    numSymbol = 0
    
    # prompt the user to enter a sentence,
    # then read it in
    sentence = input("Please enter a sentence: ")
    
    print("\n",sentence)
    # scan through the sentence character by character
    # and determine what kind of character it is
    # Keep a running total of the type of character
    for oneChar in sentence:
        if oneChar.isupper():
            numUpper += 1
        elif oneChar.islower():
            numLower += 1
        elif oneChar.isspace():
            numSpace += 1
        elif oneChar.isdigit():
            numDigit += 1
        else:
            numSymbol += 1
    # print out the totals    
    print("\nNumber of uppercase letters: ", numUpper)
    print("Number of lowercase letters: ", numLower)
    print("Number of digits: ", numDigit)
    print("Number of spaces: ", numSpace)
    print("Number of symbols: ", numSymbol)
    
    # prompt the user for their first and last name,
    # then read them in
    firstName = input("\nPlease enter your first name: ")
    lastName = input("Please enter your last name: ")
    
    # concatenate first and last name, then convert
    # it all to uppercase
    fullName = firstName + lastName
    fullName = fullName.upper()
    print("\nSo, your full name is:", fullName)
    
    print("\nSorry, I did not mean to scream your name! ")
    print("Plus, your name should have a space for easy reading.")
    
    # obtain the lengths of your first name and last
    # name, then print them out
    lenFN = len(firstName)
    lenLN = len(lastName)
    print("\nYour first name has", lenFN, "letters.")
    print("Your last name has", lenLN, "letters.")
    
    # working on 'fullName' only, extract out the
    # first name and last name
    newFirstName = fullName[:lenFN]  # slice out the first name
    newLastName = fullName[lenFN:]   # slice out the last name

    # convert all letters (except first character)
    # to lower case of first name and last name
    newFirstName = newFirstName[0:1] + newFirstName[1:].lower()
    newLastName = newLastName[0:1] + newLastName[1:].lower()
    
    # create a new full name and print it
    fullName = newFirstName + " " + newLastName
    print("\nOkay, now your full name is:", fullName)
                  
    # add symbols before and after full name and
    # print out full name
    fullName = "***" + fullName + "!!!"
    print("\nPrinting your name again:", fullName)
    print("Oops! I got overly excited. Let me fix your name again.")
    
    # now get rid of these symbols and print
    # the full name
    fullName = fullName.lstrip("*")
    print("\nCorrection almost completed:", fullName)
    fullName = fullName.rstrip("!")
    print("Finally, your full name is now:", fullName)
     
    # add prefix 'Dr. ' to full name and
    # print out full name
    fullName = fullName.replace(newFirstName, "Dr. " + newFirstName)
    print("\nAllow me to introduce: " + fullName)
    
    
    # create a list called 'allWords' from 
    # the sentence 'sentence'
    allWords = sentence.split()
    print("\nThe list allWords:")
    print(allWords)

    # call function goodBye() to end program
    goodBye()
# end function main

def goodBye():
    print("\n\nThis program was written by Aidan Underwood" + "\nEnd of program.")
# end function goodBye


# call/invoke the function main()
main()