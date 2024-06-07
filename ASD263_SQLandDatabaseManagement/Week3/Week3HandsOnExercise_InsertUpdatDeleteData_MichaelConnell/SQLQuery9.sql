-- Insert rows from the Students table into the GradStudents table for students who have graduated
INSERT INTO GradStudents (StudentID, LastName, FirstName, EnrollmentDate, GraduationDate)
SELECT StudentID, LastName, FirstName, EnrollmentDate, GraduationDate 
FROM Students 
WHERE GraduationDate IS NOT NULL;
