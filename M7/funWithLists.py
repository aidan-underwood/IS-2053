# File: funWithLists.py
#
# Purpose: To see how different lists can manipulated
#          using various functions and methods in
#          Python.
#
# Programmer: Aidan Underwood

import random

def main():
    # declare variables to be used in program
    aList1 = [0,0,0,0,0,0,0]
    aList2 = [346,210,102]
    multiList = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    # obtain the size of the list 'aList1'
    # and print it
    sizeList1 = len(aList1)
    print("Size of list aList1: ", sizeList1)
    # populate the list 'aList1' with
    # random numbers
    for i in range(0, sizeList1):
        aList1[i] = random.randint(1,50)
    # print the list 'aList1'
    print("List aList1: ", aList1, "\n")
    # call function 'printList()' to
    # print out contents of 'aList1'
    printList(aList1)
    # call function 'modifyList' to
    # modify the contents of 'aList1'
    modifyList(aList1)
    # print the list 'aList1'
    print("\n\nList aList1 modified: ")
    # call the function 'printList()' to
    # print out contents of 'aList1'
    printList(aList1)
    # print out the contents of 'aList2'
    print("\naList2:")
    print(aList2, "\n")
    # call function 'createNewList()' to create
    # a new list and assign it to 'aList3',
    # then print it
    aList3 = createNewList(aList1, aList2)
    print("List aList3: ")
    print(aList3, "\n")
    # obtain a slice of 'aList3'
    # and then print it out
    smallList = aList3[1:5]
    print("Sliced lst from aList3 [1:5]: ")
    print(smallList, "\n")
    # print out the list 'aList3'
    print("Here is aList3: ")
    print(aList3, "\n")
    # call function 'searchForNumbers()' to look
    # for random numbers that may be in the list
    print("Random numbers found in aList3: ")
    searchForNumbers(aList3)
    # call function 'searchForIndex()' to look 
    # for random numbers that may be in the list
    # 'aList3' but this time use their index to
    # update their value
    print("\nRandom numbers found in aList3 with their index: ")
    searchForIndex(aList3)
    print("\nHere is aList3: ")
    
    # print out the list 'aList3'
    print(aList3)
    # append a number to the end of
    # the list 'aList3', then print it
    aList3.append(35)
    print("\nHere is aList3: ")
    print(aList3)
    print("Now size of aList3: ", len(aList3), "\n")
    # insert a number to an exact location
    # with the list 'aList3'; choose any 
    # number between 0 and len(0,len(aList3) - 1)
    # then print the list 'aList3'
    location = random.randint(0,len(aList3) - 1)
    randomNum = random.randint(1,50)
    aList3.insert(location, randomNum)
    print("Here is aList3 with inserted value",randomNum,"at location", location, ":")
    print(aList3, "\n")
    # call function 'removeNumber()' to remove
    # random numbers that may be in 'aList3'
    # then print the list 'aList3'
    removeNumber(aList3)
    print("\nHere is aList3 after removing random numbers: ")
    print(aList3)
    print("Size of aList3 now: ", len(aList3), "\n")
    # delete a number from the 'aList3'
    # at position 'location'; choose any
    # number between 0 and len(aList3) - 1
    # then print the list 'aList3'
    location = random.randint(0, len(aList3) - 1)
    print("Here is aList3 before deleting value", aList3[location],"at location", location, ":")
    print(aList3)
    del aList3[location]
    print("Here is aList3 after deleting value at location", location, ":")
    print(aList3)
    print("Size of aList3 now: ", len(aList3), "\n")
    # copy 'aList3' into 'copiedList'
    # then print the list 'copiedList'
    copiedList = aList3
    print("Here is copiedList: ")
    print(copiedList, "\n")
    # generate a random number and append it
    # to 'aList3', then print out the lists
    # 'aList3' and 'copiedLlist'
    randomNum = random.randint(1,50)
    aList3.append(randomNum)
    print("Here is aList3 after appending random number", randomNum, ":")
    print(aList3)
    print("Here is copiedList after aList3 was modified: ")
    print(copiedList, "\n")
    
    # seperate the lists 'aList3' and 'copiedList'
    copiedList2 = [0,0,0,0,0,0,0,0,0,0,0,0]
    sizeList = len(aList3)
    
    for i in range(sizeList):
        copiedList2[i] = aList3[i]
    
    randomNumber = random.randint(1,50)
    aList3.append(randomNumber)
    print("Here is aList3 after appending random number", randomNumber, ":")
    print(aList3)
    print("Here is copiedList2 after aList3 was modified: ")
    print(copiedList2, "\n")
    
    # obtain the smallest and largest numbers
    # in 'aList3' and print them out
    print("Smallest number in aList3: ", min(aList3))
    print("Largest number in aList3: ", max(aList3), "\n")
    # sort the list 'aList3' then
    # print it out
    print("Here is aList3 unsorted: ")
    print(aList3)
    print("Here is aList3 sorted: ")
    aList3.sort()
    print(aList3, "\n")
    # reverse the order of 'aList3' then
    # print it out
    print("Here is aList3 reversed: ")
    aList3.reverse()
    print(aList3, "\n")
    # call the function 'populateMultiList() to
    # populate the 'multiList' with random numbers
    populateMultiList(multiList)
    # print the list 'multiList'
    print("Multilist populated:")
    print(multiList)
    # print the list 'multiList' again
    print("\nMultilist printed again:")
    printMultiList(multiList)
 
    # call function goodBye() to end program
    goodBye()
    
    
# end function main 

def printList(list):
    listLen = len(list)
    for i in range(listLen):
        print(list[i], end = " ")
# end function printList

def goodBye():
    print("\nThis program was written by Aidan Underwood" + "\nEnd of program.")
# end function goodBye

def printMultiList(multiList):
    for i in range(len(multiList)):
        for j in range(len(multiList[i])):
            print(multiList[i][j], end = " ")
        print()
# end function printMultiList

def populateMultiList(multiList):
    for i in range(len(multiList)):
        for j in range(len(multiList[i])):
            multiList[i][j] = random.randint(1,100)
# end function populateMultiList

def removeNumber(list):
    listLen = len(list)
    for i in range(listLen):
        num = random.randint(1,100)
        try:
            list.remove(num)
            print("removed:", num)
        except ValueError:
            print("could not remove nonexisting number:", num)
# end function removeNumber

def searchForIndex(list):
    for i in range(len(list)):
        num = random.randint(1,100)
        
        try:
            location = list.index(num)
            list[location] = list[location] * 3
            print("found:", num, "at index:", location, "it has a new value of:", list[location])
        except ValueError:
            print("not found:", num)
# end function searchForIndex
   
def searchForNumbers(list):
    for i in range(len(list)):
        num = random.randint(1,100)
        if num in list:
            print("found:", num)
    print()
# end function searchForNumbers

def createNewList(list1, list2):
    return list2 + list1
# end function createNewList

def modifyList(list):
    listLen = len(list)
    for i in range(listLen):
        list[i] = list[i] * 2
# end function modifyList

# call/invoke the function main()
main()