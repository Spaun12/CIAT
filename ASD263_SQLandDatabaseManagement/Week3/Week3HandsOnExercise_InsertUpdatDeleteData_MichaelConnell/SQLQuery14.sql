-- Retrieve the records for instructors in the Education department
SELECT * FROM Instructors 
WHERE DepartmentID = (SELECT DepartmentID FROM Departments WHERE DepartmentName = 'Education');
