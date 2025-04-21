# File: retailTester.py
# 
# Purpose: To create two objects from the class RetailItem.
#          Then print out each object's information.
#          Modify an attribute from each object and print
#          out the object's information again.  Pass the
#          objects to a function call 'printByAccessor()'
#          to print out the object's information.
#
# Programmer: Aidan Underwood

# Files: retail.py and retailTester.py

import retail

def main():
    # instantiate (create) two objects from
    # the class 'RetailItem'
    item1 = retail.RetailItem("Jacket", 12, 59.95)
    item2 = retail.RetailItem("Designer Jeans", 40, 34.95)

    # using accessor methods print out each object's info
    print("Printing via accessor methods:")
    print("==============================")
    print("Retail item 1:", "\nDescription:", item1.getDescription(),
          "\nNumber in inventory:", item1.getInventory(),
          "\nPrice: $", format(item1.getPrice(), ",.2f"))
    
    print("\nRetail item 2:", "\nDescription:", item2.getDescription(),
          "\nNumber in inventory:", item2.getInventory(),
          "\nPrice: $", format(item2.getPrice(), ",.2f"))

    # passing an object to a function for printing
    # via accessor methods
    print("\nNow printing by passing the object to a function:")
    print("===================================================")
    printByAccessor(item1)
    printByAccessor(item2)
    
    # change inventory of 'item1' to be 10
    item1.setInventory(10)
    
    # change price of 'item2' to be 30.55
    item2.setPrice(30.55)
        
    # passing an object to a function for printing
    # via accessor methods
    print("\nNow printing by passing the object to a function:")
    print("===================================================")
    printByAccessor(item1)
    printByAccessor(item2)
    

    # print out each object's info via the __str()__ method
    print("\nPrinting via the __str__() method:")
    print("====================================")
    print("\nRetail item 1: ")
    print(item1) # implicit call to __str__ method
    print("\nRetail item 2: ")
    print(item2.__str__()) # explicit call to __str__ method

    # call function goodBye() to end program
    goodBye()  
# end function main

def printByAccessor(anItem):
    # print out this item information by calling the object's accessor methods
    print("\nRetail item:", "\nDescription:", anItem.getDescription(),
          "\nNumber in inventory:", anItem.getInventory(),
          "\nPrice: $", format(anItem.getPrice(), ",.2f"))
# end function printByAccessor
    
def goodBye():
    print("\nThis program was written by Aidan Underwood" + "\nEnd of program.")
# end function goodBye

# call/invoke the function main()
main()