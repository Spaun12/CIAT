# Week 3 Hands On Course Information Michael Connell
# create the course to room dictionary
course_to_room = {
    'CS101': '3004',
    'CS102': '4501',
    'CS103': '6755',
    'NT110': '1244',
    'CM241': '1411'
}
#I just learned you could place {} in this way for coding readability. Cool.
# create the course to instructor dictionary
course_to_instructor = {
    'CS101': 'Haynes',
    'CS102': 'Alvarado',
    'CS103': 'Rich',
    'NT110': 'Burke',
    'CM241': 'Lee'
}
# create the course to meeting time dictionary
course_to_meeting_time = {
    'CS101': '8:00 a.m.',
    'CS102': '9:00 a.m.',
    'CS103': '10:00 a.m.',
    'NT110': '11:00 a.m.',
    'CM241': '1:00 p.m.'
}
# loop until the user chooses to exit
while True:
    # prompt user to enter a course number
    course_number = input('Enter a course number: ')
    # check if the course number is valid
    if course_number in course_to_room:
        # retrieve the room number, instructor, and meeting time for the given course
        room_number = course_to_room[course_number]
        instructor = course_to_instructor[course_number]
        meeting_time = course_to_meeting_time[course_number]
        # display the information to the user
        print(f'Course Number: {course_number}')
        print(f'Room Number: {room_number}')
        print(f'Instructor: {instructor}')
        print(f'Meeting Time: {meeting_time}')
    else:
        print('Invalid course number')

    # ask the user if they want to look up another course
    response = input('Would you like to look up another course? (y/n): ')
    if response.lower() != 'y':
        break
