-- Increase the annual salary for all instructors in the Education department by 5%
UPDATE Instructors 
SET AnnualSalary = AnnualSalary * 1.05 
WHERE DepartmentID = (SELECT DepartmentID FROM Departments WHERE DepartmentName = 'Education');
