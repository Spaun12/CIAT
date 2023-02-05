#possible bones for a student enrollment program

# Collect student information
name = input("Enter the student's name: ")
address = input("Enter the student's address: ")

while True:
    telephone = input("Enter the student's telephone number: ")
    if telephone.isnumeric() and len(telephone)==10:
        break
    else:
        print("Please enter a valid telephone number")

while True:
    grade_level = input("Enter the student's grade level: ")
    if grade_level in ["Freshman", "Sophomore", "Junior", "Senior"]:
        break
    else:
        print("Please enter a valid grade level (Freshman, Sophomore, Junior, Senior)")

status = input("Is the student a new or transfer student? ")

# Collect variable number of courses
course_selections = []
while True:
    course = input("Enter a course name (or 'done' to finish): ")
    if course.lower() == "done":
        break
    course_selections.append(course)

# Print enrollment information
print("Student Name: " + name.title() + "\nAddress: " + address + "\nTelephone: " + telephone + "\nGrade Level: " + grade_level + "\nStatus: " + status)
if len(course_selections)>0:
    print("Course Selections:")
    for course in course_selections:
        print("- " + course.title())
        