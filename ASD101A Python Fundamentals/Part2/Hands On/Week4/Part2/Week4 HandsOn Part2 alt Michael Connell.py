#Week4 HandsOn Part2 alt Michael Connell
import csv

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

# Prompt the user to enter information for at least two friends or family members
people = []
while True:
    print("Enter information for a friend or family member:")
    name = input("Name: ")
    address = input("Address: ")
    age = int(input("Age: "))
    phone_number = input("Phone number: ")
    relation = input("Friend or family member: ")
    people.append((name, address, age, phone_number, relation))
    print()
    
    # Ask the user if they want to add another contact
    another = input("Do you want to add another contact? (y/n): ")
    if another.lower() == 'n':
        break

# Save the information to a CSV file
filename = 'personal_information.csv'
with open(filename, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Name', 'Address', 'Age', 'Phone Number', 'Relation'])
    for person in people:
        writer.writerow(person)

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
        
        for person in people:
            print("Name:           ", person[0])
            print("Address:        ", person[1])
            print("Age:            ", person[2])
            print("Phone number:   ", person[3])
            print("Relation:       ", person[4])
            print("\n")
        break
    elif display.lower() == 'n':
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'")