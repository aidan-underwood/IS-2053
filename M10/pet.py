class Pet:
    def __init__(self, nameIn, animalTypeIn, ageIn):
        # set up default values for each data attribute
        # (i.e., instance fields/instance variables)
        self.__name = nameIn
        self.__animalType = animalTypeIn
        self.__age = ageIn
        self.fur = "fluffy"
        
    # end __init__
    
    # mutator methods
    def setName(self, nameIn):
        self.__name = nameIn
    # end method setName
    
    def setAnimalType(self, animalTypeIn):
        self.__animalType = animalTypeIn
    # end method setAnimalType
    
    def setAge(self, ageIn):
        self.__age = ageIn
    # end method setAge
    
    # accessor methods
    def getName(self):
        return self.__name
    # end method getName
    
    def getAnimalType(self):
        return self.__animalType
    # end method getAnimalType
    
    def getAge(self):
        return self.__age
    # end method getAge
    
    def goodBye(self):
        print("\nBye from:", self.getName() + "!")
    # end method goodBye
    
# end class Pet
