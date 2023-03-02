#Week4 HandsOn Part2 Michael Connell
class PersonalInformation:
    def __init__(self, name, address, age, phone_number):
        # Initialize the class with the given personal information
        self.name = name
        self.address = address
        self.age = age
        self.phone_number = phone_number
    # Accessor methods to get the personal information
    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

    def get_age(self):
        return self.age

    def get_phone_number(self):
        return self.phone_number
    # Mutator methods to set the personal information
    def set_name(self, name):
        self.name = name

    def set_address(self, address):
        self.address = address

    def set_age(self, age):
        self.age = age

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number
# Prompt the user to enter their personal information
print("Enter your personal information:")
name = input("Name: ")
address = input("Address: ")
age = int(input("Age: "))
phone_number = input("Phone number: ")
my_info = PersonalInformation(name, address, age, phone_number)
print()
# Prompt the user to enter information for two friends or family members
print("Enter information for friend 1:")
friend1_name = input("Name: ")
friend1_address = input("Address: ")
friend1_age = int(input("Age: "))
friend1_phone_number = input("Phone number: ")
friend1_info = PersonalInformation(friend1_name, friend1_address, friend1_age, friend1_phone_number)
print()

print("Enter information for friend 2:")
friend2_name = input("Name: ")
friend2_address = input("Address: ")
friend2_age = int(input("Age: "))
friend2_phone_number = input("Phone number: ")
friend2_info = PersonalInformation(friend2_name, friend2_address, friend2_age, friend2_phone_number)
print()
# Prompt the user to choose whether to display the personal information
while True:
    display = input("Would you like to display the personal information? (y/n): ")
    if display.lower() == 'y':
        # Display the personal information for each instance in a readable format with a space between each instance
        print("Personal Information:")
        print("------------------------------------------------------")
        print("Name:           ", my_info.get_name())
        print("Address:        ", my_info.get_address())
        print("Age:            ", my_info.get_age())
        print("Phone number:   ", my_info.get_phone_number())
        print("\n")

        print("Name:           ", friend1_info.get_name())
        print("Address:        ", friend1_info.get_address())
        print("Age:            ", friend1_info.get_age())
        print("Phone number:   ", friend1_info.get_phone_number())
        print("\n")

        print("Name:           ", friend2_info.get_name())
        print("Address:        ", friend2_info.get_address())
        print("Age:            ", friend2_info.get_age())
        print("Phone number:   ", friend2_info.get_phone_number())
        break
    elif display.lower() == 'n':
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'") 