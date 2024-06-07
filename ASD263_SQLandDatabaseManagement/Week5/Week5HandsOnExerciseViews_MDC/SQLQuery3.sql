-- Update the annual salary for full-time instructors in the English department
UPDATE Instructors
SET AnnualSalary = AnnualSalary * 1.10
FROM Instructors i
JOIN Departments d ON i.DepartmentID = d.DepartmentID
WHERE d.DepartmentName = 'English' AND i.Status = 'F';
