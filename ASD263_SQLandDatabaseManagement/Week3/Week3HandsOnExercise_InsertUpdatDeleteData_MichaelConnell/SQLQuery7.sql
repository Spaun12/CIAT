-- Delete instructors who aren’t teaching any courses
DELETE FROM Instructors 
WHERE InstructorID NOT IN (SELECT DISTINCT InstructorID FROM Courses);
