class Pet:
    def __init__(self, name, animal_type, age):
        # Initialize instance variables with given values
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age
        
    def set_values(self):
        # Prompt user for pet name, type, and age
        self.__name = input("What is the name of your pet? ")
        self.__animal_type = input(f"What type of animal is {self.__name}? ")
        self.__age = input(f"How old is {self.__name}? ")
        
    def set_name(self, name):
        # Update the name instance variable with the given name
        self.__name = name
    
    def set_animal_type(self, animal_type):
        # Update the animal_type instance variable with the given animal type
        self.__animal_type = animal_type
    
    def set_age(self, age):
        # Update the age instance variable with the given age
        self.__age = age
    
    def get_name(self):
        # Return the value of the name instance variable
        return self.__name
    
    def get_animal_type(self):
        # Return the value of the animal_type instance variable
        return self.__animal_type
    
    def get_age(self):
        # Return the value of the age instance variable
        return self.__age
    
    def __str__(self):
        # Return a string representation of the object
        return f"{self.__name} is a {self.__animal_type} and is {self.__age} years old"
    

# Create a new Pet object with name "Fido", animal type "dog", and age "2"
myPet = Pet("Fido", "dog", "2")

# Call the get_name, get_animal_type, and __str__ methods on myPet and print the results
print(myPet.get_name())
print(myPet.get_animal_type())
print(myPet)

# Create a new Pet object with name "Tiffane", animal type "cat", and age "2"
myPet2 = Pet("Tiffane", "cat", "2")

# Call the __str__ method on myPet2 and print the result
print(myPet2)
