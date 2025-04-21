# File: retail.py
# 
# Purpose: Creates a class called RetailItem and have three
#          data attributes (instance fields/instance 
#          variables).  Accessor and mutator methods are
#          created.  The str() method is also created.
#
# Programmer: Aidan Underwood
# 
# Files: retail.py and retailTester.py

class RetailItem:
    def __init__(self, description="", inventory=0, price=0.0):
        # set up default values for each data attribute
        # (i.e., instance fields/instance variables)
        self.__description = description
        self.__inventory = inventory
        self.__price = price
    # end constructor

    # mutator methods

    def setDescription(self, description):
        self.__description = description
    # end method setDescription

    def setInventory(self, inventory):
        self.__inventory = inventory
    # end method setInventory

    def setPrice(self, price):
        self.__price = price
    # end method setPrice
        
    # accessor methods

    def getDescription(self):
        return self.__description
    # end method getDescription

    def getInventory(self):
        return self.__inventory
    # end method getInventory

    def getPrice(self):
        return self.__price
    # end method getPrice

    # str method
    def __str__(self):
        result = "Description: " + self.getDescription() + "\n" + "Units in inventory: " + str(self.getInventory()) + "\n" + "Price: $" + str(format(self.getPrice(), ",.2f"))
        return result
    # end method __str__()
# end class RetailItem