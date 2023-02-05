#Professor Class Discussion Challenge Version 2

import tkinter as tk

# create a form
root = tk.Tk()
root.title("Student Enrollment")
root.geometry("500x500")

# create variables to store student information
name = tk.StringVar()
address = tk.StringVar()
telephone = tk.StringVar()
selected_grade_level = tk.StringVar()
selected_status = tk.StringVar()
selected_course1 = tk.StringVar()
selected_course2 = tk.StringVar()

# create a list of available grades
available_grades = ["Freshman", "Sophomore", "Junior", "Senior"]
# create a list of available status
available_status = ["New", "Transfer"]
# create a list of available courses
available_courses = ["Math", "Science", "English", "P.E.", "Elective1", "Elective2"]

# create labels and text boxes for student name, address, and telephone
name_label = tk.Label(root, text="Name:")
name_label.pack()
name_entry = tk.Entry(root, textvariable=name)
name_entry.pack()

address_label = tk.Label(root, text="Address:")
address_label.pack()
address_entry = tk.Entry(root, textvariable=address)
address_entry.pack()

telephone_label = tk.Label(root, text="Telephone:")
telephone_label.pack()
telephone_entry = tk.Entry(root, textvariable=telephone)
telephone_entry.pack()

# create a drop-down menu for grade level
grade_level_dropdown = tk.OptionMenu(root, selected_grade_level, *available_grades)
grade_level_dropdown.pack()

# create a drop-down menu for status
status_dropdown = tk.OptionMenu(root, selected_status, *available_status)
status_dropdown.pack()

# create two drop-down menus for course selection
course1_dropdown = tk.OptionMenu(root, selected_course1, *available_courses)
course1_dropdown.pack()
course2_dropdown = tk.OptionMenu(root, selected_course2, *available_courses)
course2_dropdown.pack()

# create a submit button to show the enrollment information
submit_button = tk.Button(root, text="Submit", command=lambda: 
                                                        print("Student Name:", name.get().title(), 
                                                        "\nAddress:", address.get(), 
                                                        "\nTelephone:", telephone.get(), 
                                                        "\nGrade Level:", selected_grade_level.get(), 
                                                        "\nStatus:", selected_status.get(), 
                                                        "\nCourse Selection:",selected_course1.get().title(),",",selected_course2.get().title()))
submit_button
