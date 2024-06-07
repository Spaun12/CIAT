USE Examples;

SELECT d.DeptNo, DeptName, EmployeeID, LastName
FROM Departments d, Employees e
ORDER BY d.DeptNo;

