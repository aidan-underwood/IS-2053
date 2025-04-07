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
    
    # print out the roller coaster names
        
    # delete an item from 'rollerCoasters', then
    # print out the dictionary
    
    # pop an item from the dictionaries and then
    # print them out
    
    # print out the dictionaries
    
    # clear out all of our dictionaries
    
    # print out all dictionaries

    # call function goodBye() to end program
    
# end function main


# end function goodBye

# invoke/call the function main()
main()