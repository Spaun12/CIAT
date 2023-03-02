#Week4 HandsOn Part1 Michael Connell
# Define the Pet class with attributes and methods
class Pet:
    def __init__(self, name, animal_type, age):
        # Initialize the attributes with the provided values
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    def set_name(self, name):
        # Set the pet's name attribute
        self.__name = name

    def set_animal_type(self, animal_type):
        # Set the pet's animal type attribute
        self.__animal_type = animal_type

    def set_age(self, age):
        # Set the pet's age attribute
        self.__age = age

    def get_name(self):
        # Return the pet's name attribute
        return self.__name

    def get_animal_type(self):
        # Return the pet's animal type attribute
        return self.__animal_type

    def get_age(self):
        # Return the pet's age attribute
        return self.__age

# Create a new Pet object
my_pet = Pet("", "", 0)

# Prompt the user for information
name = input("Enter your pet's name: ")
animal_type = input("Enter the animal type of your pet: ")
age = int(input("Enter your pet's age: "))

# Set the object's attributes using the setter methods
my_pet.set_name(name)
my_pet.set_animal_type(animal_type)
my_pet.set_age(age)

# Display the pet's information using the getter methods
print("Your pet's name is", my_pet.get_name())
print("Your pet's animal type is", my_pet.get_animal_type())
print("Your pet's age is", my_pet.get_age())