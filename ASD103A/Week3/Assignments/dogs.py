"""Michael Connell Week3 Assignment - Inheritance 2023-06-09"""

"""FIrst: Identify the common attributes and behaviors among all classes.
Second: Create a base class that defines these common attributes and behaviors.
Third: If any class has unique attributes or behaviors, it can inherit from the base class and add/override these unique aspects.
Fourth: If a class doesn't have any unique attribute or behavior, it can just inherit from the base class without adding anything new."""

# Base class Dog which has all the common features and behaviors of a dog
class Dog:
    def __init__(self, name):
        self.name = name  

    def speak(self):
        # Including the class name (breed) and the dog's name in the output
        print(f"{self.__class__.__name__} named {self.name} says: hello, bark!")
	
    def likes_walks(self):
        return True

# Poodle class inherits from Dog
class Poodle(Dog):
    # since none of the current dogs have any unique attribute or behavior, it doesn't need any unique methods, so pass
    pass

# GoldenRetriever class inherits from Dog
class GoldenRetriever(Dog):
    pass

# Samoyed class inherits from Dog
class Samoyed(Dog):
    pass

		
