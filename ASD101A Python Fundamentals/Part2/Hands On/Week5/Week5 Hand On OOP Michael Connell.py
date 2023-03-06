#Week5 Hand On OOP Michael Connell
class Employee:
    """
    Represents an employee with a name, ID number, department, and job title.
    
     _____________________________
    |          Employee           |
    |-----------------------------|
    | - name: str                 |
    | - id_number: int            |
    | - department: str           |
    | - job_title: str            |
    |-----------------------------|
    | + __init__(name: str,       |
    |            id_number: int,  |
    |            department: str, |
    |            job_title: str)  |
    | + display_employee()        |
     -----------------------------
    """
    #This is the UML diagram for the Employee class.
    def __init__(self, name: str, id_number: int, department: str, job_title: str):
        """
        Initializes the attributes of the Employee class with the given values.
        """
        self.__name = name
        self.__id_number = id_number
        self.__department = department
        self.__job_title = job_title
        
    def display_employee(self):
        """
        Formats and prints the employee data in a table.
        """
        print("|{:<15}|{:<15}|{:<15}|{:<15}|".format(self.__name, self.__id_number, self.__department, self.__job_title))

# Testing the Employee class
employee1 = Employee("Susan Meyers", 47899, "Accounting", "Vice President")
employee2 = Employee("Mark Jones", 39119, "IT", "Programmer")
employee3 = Employee("Joy Rogers", 81774, "Manufacturing", "Engineer")

# Displaying the employee data in a formatted table
print("-" * 65)
print("|{:<15}|{:<15}|{:<15}|{:<15}|".format("Name", "ID Number", "Department", "Job Title"))
print("-" * 65)
employee1.display_employee()
employee2.display_employee()
employee3.display_employee()
print("-" * 65)