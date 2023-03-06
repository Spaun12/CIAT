#Week 5 Discussion Board Michael Connell
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    # Accessor method for name
    def get_name(self):
        return self.__name
    
    # Accessor method for age
    def get_age(self):
        return self.__age
    
    # Mutator method for name
    def set_name(self, name):
        self.__name = name
    
    # Mutator method for age
    def set_age(self, age):
        self.__age = age

# Creating an instance of the Person class with initial values
person = Person("John", 30)

# Accessing object's state using accessor methods
print(person.get_name())  
print(person.get_age())   

# Modifying object's state using mutator methods
person.set_name("Jane")
person.set_age(35)

# Accessing modified state using accessor methods
print(person.get_name())  
print(person.get_age())   