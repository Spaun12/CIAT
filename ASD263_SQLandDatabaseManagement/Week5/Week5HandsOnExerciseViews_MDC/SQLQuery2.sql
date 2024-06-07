-- Select full-time instructors in the English department
SELECT *
FROM DepartmentInstructors
WHERE DepartmentName = 'English' AND Status = 'F';
