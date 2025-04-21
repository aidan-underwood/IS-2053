# File: uniqueWords.py
# 
# Purpose: Opens a file whose contents will be read in
#          and printed.  Extract all of the words from 
#          the text to create a list and print it.  A
#          set is created from this list to obtain all
#          of the unique words and print them out each
#          per line.
#
# Programmer: Aidan Underwood

def main():
    # hard code the name of the file for an
    # academic example
    fileInput = "myWords.txt"
    # read in the entire and then print it
    inputFile = open(fileInput, "r")
    text = inputFile.read()
    print(text)
    
    # close the file
    inputFile.close()
    
    # extract out all of the words of the words that
    # were read in and print them out
    allWords = text.split()
    print("\nAll of the words:\n", allWords, "\n")
    
    totalWords = len(allWords)
    print("There are", totalWords, "words that were read in from the file.\n")
    # using a set, obtain all the unique words
    # that were read in from the file
    uniqueWords = set(allWords)
    num = len(uniqueWords)
    
    for word in uniqueWords:
        print(word)

    print("\nThere were", num, "unique words out of a toal of", totalWords, "words.")
    # call function goodBye() to end program       
    goodBye()    
# end function main

def goodBye():
    print("\nThis program was written by Aidan Underwood" + "\nEnd of program.")
# end function goodBye

# invoke/call the function main()
main()