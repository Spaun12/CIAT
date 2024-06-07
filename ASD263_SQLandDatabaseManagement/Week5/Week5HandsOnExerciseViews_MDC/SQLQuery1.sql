-- Create the view DepartmentInstructors
CREATE VIEW DepartmentInstructors AS
SELECT 
    d.DepartmentName,
    i.LastName,
    i.FirstName,
    i.Status,
    i.AnnualSalary
FROM 
    Departments d
JOIN 
    Instructors i ON d.DepartmentID = i.DepartmentID;
