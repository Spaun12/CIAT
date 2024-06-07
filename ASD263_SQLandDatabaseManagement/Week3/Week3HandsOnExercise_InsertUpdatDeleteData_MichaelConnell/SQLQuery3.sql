-- Update the annual salary for Susan Benedict
UPDATE Instructors 
SET AnnualSalary = 35000.00 
WHERE InstructorID = (SELECT MIN(InstructorID) FROM Instructors WHERE LastName = 'Benedict');
