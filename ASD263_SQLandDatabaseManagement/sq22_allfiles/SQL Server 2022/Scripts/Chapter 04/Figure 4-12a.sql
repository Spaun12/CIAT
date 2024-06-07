USE Examples;

SELECT d.DeptNo, DeptName, EmployeeID, LastName
FROM Departments d
    CROSS JOIN Employees e
ORDER BY d.DeptNo;

