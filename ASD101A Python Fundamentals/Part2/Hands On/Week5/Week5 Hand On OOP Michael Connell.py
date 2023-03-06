#Week5 Hand On OOP Michael Connell
class Employee:
    def __init__(self, name, id_number, department, job_title):
        self.name = name
        self.id_number = id_number
        self.department = department
        self.job_title = job_title
        
    def display_employee(self):
        # Format and print the employee data in a table
        print("|{:<15}|{:<15}|{:<15}|{:<15}|".format(self.name, self.id_number, self.department, self.job_title))

# Create three Employee objects with the given data
employee1 = Employee("Susan Meyers", 47899, "Accounting", "Vice President")
employee2 = Employee("Mark Jones", 39119, "IT", "Programmer")
employee3 = Employee("Joy Rogers", 81774, "Manufacturing", "Engineer")

# Display the employee data in a formatted table
print("-"*65)
print("|{:<15}|{:<15}|{:<15}|{:<15}|".format("Name", "ID Number", "Department", "Job Title"))
print("-"*65)
employee1.display_employee()
employee2.display_employee()
employee3.display_employee()
print("-"*65)