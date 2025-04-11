# File: funWithSets.py
# 
# Purpose: To create and perform various operations on
#          different sets.
#
# Programmer: Aidan Underwood

def main():
    # create sets
    set1 = set(["green", "red", "blue", "red"])
    set2 = set([7,1,2,23,2,4,5])
    set3 = set(["green", "yellow"])
    
    # print out sets
    print("set1:", set1)
    print("set2:", set2)
    print("set3:", set3)
    
    # does a color (red) exist wtih 'set1'?   
    if "red" in set1:
        print("\nred is in set1")
    else:  
        print("\nred is not in set1")
        
    # obtain the lengths of the sets
    lenSet = len(set1)
    print("\nThere are", lenSet, "items in set1")
    
    lenSet = len(set2)
    print("There are", lenSet, "items in set2")
    
    lenSet = len(set3)
    print("There are", lenSet, "items in set3")
    
    # various function usage
    print("\nmax in set2 is", max(set2))
    print("min in set2 is", min(set2))
    print("sum of set2 is", sum(set2))
    
    # union of set1 and set3
    set4 = set1.union(set3)
    print("\nunion of set1 and set3", set4)
    
    # difference between set1 and set3
    set4 = set1.difference(set3)
    print("difference between set1 and set3", set4)
    
    # intersection of set1 and set3
    set4 = set1.intersection(set3)
    print("intersection between set1 and set3", set4)

    # add a color to set1
    set1.add("yellow")
    print("\nyellow was added to set1:")
    print(set1)
        
    # remove a color from set1
    set1.remove("yellow")
    print("\nyellow was removed from set1:")
    print(set1)
    
    # call function goodBye() to end program   
    goodBye() 
# end function main

def goodBye():
    print("\nThis program was written by Aidan Underwood" + "\nEnd of program.")
# end function goodBye

# call/invoke the function main()
main()