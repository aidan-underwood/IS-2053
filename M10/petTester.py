# File: petTester.py
# 
# Purpose: Prompts the user to enter pet information
#          and instantiates objects from a user
#          defined class called Pet.  The pet 
#          information is then printed using 
#          methods created in the class Pet.
#
# Programmer: Aidan Underwood
#
# Files: petTester.py and pet.py

import pet

def main():
    # prompt the user for pet name, type of
    # animal, and its age.  Then read them
    # all in, respectively
    petName = input("Enter the name of the pet: ")
    petType = input("Enter the type of animal the pet is: ")
    petAge = int(input("Enter the age (integer) of the pet: "))
    
    # instantiate an object from the Pet class
    myPet1 = pet.Pet(petName, petType, petAge)
    
    # print out the pet information via the 
    # methods from the Pet class
    print("\nAnimal Information:")
    print("Pet1 name:", myPet1.getName())
    print("Pet1 animal type:", myPet1.getAnimalType())
    print("Pet1 age:", myPet1.getAge())
    
    # attempt to access an attribute/instance field
    print("Fur type is: ", myPet1.fur)
    
    # prompt the user for another pet name,
    # type of animal, and its age.  Then
    # read them all in, respectively
    petName2 = input("\nEnter the name of the pet: ")
    petType2 = input("Enter the type of animal the pet is: ")
    petAge2 = int(input("Enter the age (integer) of the pet: "))
    
    # instantiate another object from the Pet class
    myPet2 = pet.Pet(petName2, petType2, petAge2)
    
    # print out the pet information via the 
    # methods from the Pet class
    print("\nAnimal Information:")
    print("Pet2 name:", myPet2.getName())
    print("Pet2 animal type:", myPet2.getAnimalType())
    print("Pet2 age:", myPet2.getAge(), "years")
    
    # change the attributes of Pet2
    myPet2.setName("Pokey")
    myPet2.setAnimalType("Goldfish")
    myPet2.setAge(6)
    
    print("\nUpdated animal information for Pet2:")
    print("Pet2 name:", myPet2.getName())
    print("Pet2 animal type:", myPet2.getAnimalType())
    print("Pet2 age:", myPet2.getAge(), "years")
    
    # have the pets say bye
    print("\nBye from:", myPet1.getName() + "!")
    print("Bye from:", myPet2.getName() + "!")
    
    # call function goodBye() to end program
    goodBye()
# end function main

def goodBye():
    print("\nThis program was written by Aidan Underwood" + "\nEnd of program.")
# end function goodBye

# invoke/call the function main()
main()