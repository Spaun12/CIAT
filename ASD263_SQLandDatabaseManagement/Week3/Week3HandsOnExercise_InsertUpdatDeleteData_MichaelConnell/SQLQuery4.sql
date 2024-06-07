-- Delete the instructor with the last name Adams
DELETE FROM Instructors 
WHERE InstructorID = (SELECT MAX(InstructorID) FROM Instructors WHERE LastName = 'Adams');
