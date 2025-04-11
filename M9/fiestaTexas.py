# File: fiestaTexas.py
# 
# Purpose: Four dictionaries are created about four
#          roller coasters at Fiesta Texas.  Operations
#          are performed on these dictionaries.
#
# Programmer: Aidan Underwood

def main():
    # set up our dictionaries about the roller coasters
    rollerCoasters = {"Name1":"Rattler", "Name2":"Superman", "Name3":"Goliath", "Name4":"Roadrunner Express"}
    speed = {"Name1": 70, "Name2": 70, "Name3": 50, "Name4": 35}
    height = {"Name1": 179, "Name2": 168, "Name3": 105, "Name4": 73}
    length = {"Name1": 3266, "Name2": 4025, "Name3": 2693, "Name4": 2400}
    aName = "Name3"
    
    
    # print out a header
    print("Fiesta Texas roller coasters:\n")
    
    # print out each dictionary
    print("Roller Coasters - ", rollerCoasters)
    print("Speed of roller coasters- ", speed)
    print("Height of roller coasters - ", height)
    print("Length of roller coasters - ", length)
    
    # prompt the user to enter a key
    rc = input("\nPlease enter a roller coaster key (Name1, Name2, Name3, or Name4): ")
    
    # decide whether this roller coaster exists. If it does,
    # print out information about it, otherwise, print out
    # an error message
    if rc in rollerCoasters:
        print("\nThe roller coaster is:", rollerCoasters[rc])
        print("The max speed is:", speed[rc],"mph!")
        print("The peak height is:", height[rc],"feet!")
        print("The length is:", length[rc],"feet!")
    else:
        print("\nSorry, that roller coaster does not exist.")
    
    # get a roller coaster name using get()
    rcName = rollerCoasters.get(aName, "#")
    
    # if name is found, get other information
    if rcName != "#":
        print("\nRoller coaster with key", aName, "was found.")
        rcSpeed = speed.get(aName)
        rcHeight = height.get(aName)
        rcLength = length.get(aName)
        print("Name:", rcName)
        print("Speed:", rcSpeed)
        print("Height:", rcHeight)
        print("Length:", rcLength)
    else:
        print("\nSorry, roller coaster with key", aName, "does not exist.")
    
    # update an item in the 'rollerCoaster' dictionary
    # and add another name to it as well
    rollerCoasters["Name1"] = "Iron Rattler"
    rollerCoasters["Name5"] = "My Roller Coaster"
    
    # print out the roller coaster names
    print("\nHere are the roller coaster names only:")
    
    for key in rollerCoasters:
        print(key, rollerCoasters[key])

    # how many roller coaster names are there?
    rcLen = len(rollerCoasters)
    print("\nThere are", rcLen, "roller coasters.")
        
    # delete an item from 'rollerCoasters', then
    # print out the dictionary
    try:
        del rollerCoasters["Name5"]
    except Exception:
        print("\nError! The key that you want deleted does not exist.")
        
    print("\nAgain, here are the roller coaster names:")
    
    for key in rollerCoasters:
        print(key, rollerCoasters[key])
        
    rcLen = len(rollerCoasters)
    print("\nThere are", rcLen, "roller coasters.")
   
    # pop an item from the dictionaries and then
    # print them out
    rcName = rollerCoasters.pop(aName, "Does not exist.")
    rcSpeed = speed.pop(aName, "No speed.")
    rcHeight = height.pop(aName, "No height.")
    rcLength = length.pop(aName, "No length.")
    
    print("\nPopped items from the dictionaries:")
    print(rcName, rcSpeed, rcHeight, rcLength)
    
    # print out the dictionaries
    print("\nModified dictionaries:")
    print(rollerCoasters)
    print(speed)
    print(height)
    print(length)
    
    # clear out all of our dictionaries
    rollerCoasters.clear()
    speed.clear()
    height.clear()
    length.clear()
    
    # print out all dictionaries
    print("\nRoller coasters - ", rollerCoasters)
    print("Speed of roller coasters - ", speed)
    print("Height of roller coasters - ", height)
    print("Length of roller coasters - ", length)

    # call function goodBye() to end program
    goodBye()
# end function main

def goodBye():
    print("\nThis program was written by Aidan Underwood" + "\nEnd of program.")
# end function goodBye

# invoke/call the function main()
main()