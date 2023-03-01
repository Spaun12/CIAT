#Pet Challenge
import random

# Define the 'Pet' parent class
class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        pass

# Define the 'Trickster' child class
class Trickster:
    def __init__(self, tricks):
        self.tricks = tricks

    def do_trick(self):
        print(f"{self.species} is doing a trick: {random.choice(self.tricks)}!")

# Define a derived class 'Cat', which inherits from the 'Pet' and 'Trickster' classes
class Cat(Pet, Trickster):
    def __init__(self, name, color):
        # Call the constructor of the 'Pet' parent class using super()
        super().__init__(name, "cat")
        # Call the constructor of the 'Trickster' child class using super()
        Trickster.__init__(self, self._get_tricks())
        self.color = color

    def make_sound(self):
        sound = random.choice(["Meow!", "Purr..."])
        print(sound)

    def _get_tricks(self):
        return [
            "chasing a toy",
            "climbing a tree",
            "jumping over an obstacle",
            "scratching a post",
            "hiding and pouncing",
            "catching a mouse",
            "rolling over",
            "playing with a ball",
            "walking on a leash"
        ]

# Define a derived class 'Dog', which inherits from the 'Pet' and 'Trickster' classes
class Dog(Pet, Trickster):
    def __init__(self, name, breed):
        # Call the constructor of the 'Pet' parent class using super()
        super().__init__(name, "dog")
        # Call the constructor of the 'Trickster' child class using super()
        Trickster.__init__(self, self._get_tricks())
        self.breed = breed

    def make_sound(self):
        sound = random.choice(["Woof!", "Whine..."])
        print(sound)

    def chase_cat(self, cat):
        if isinstance(cat, Cat):
            print(f"{self.name} is chasing {cat.name}! Cats hate dogs!")
        else:
            print(f"{self.name} is chasing {cat.name}! Oops, wrong target.")

    def _get_tricks(self):
        return [
            "playing dead",
            "rolling over",
            "fetching a ball",
            "jumping through a hoop",
            "spinning in circles",
            "giving a high-five",
            "speaking on command",
            "sitting up",
            "balancing a treat on the nose"
        ]

# Create an instance of the 'Cat' class and call its methods
my_cat = Cat("Whiskers", "gray")
my_cat.make_sound()
my_cat.do_trick()
print(f"My cat's name is {my_cat.name}.")
print(f"My cat's color is {my_cat.color}.")

# Create an instance of the 'Dog' class and call its methods
my_dog = Dog("Fido", "Labrador Retriever")
my_dog.make_sound()
my_dog.do_trick()
my_dog.chase_cat(my_cat)

# Create an instance of the 'Pet' class and call its methods
my_pet = Pet("Fluffy", "cat")
my_pet.make_sound()