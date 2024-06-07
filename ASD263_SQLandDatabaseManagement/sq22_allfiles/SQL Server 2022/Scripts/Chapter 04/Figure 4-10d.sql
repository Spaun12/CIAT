USE Examples;

SELECT DeptName, LastName, ProjectNo
FROM Departments d
    LEFT JOIN Employees e
        ON d.DeptNo = e.DeptNo
    LEFT JOIN Projects p
        ON e.EmployeeID = p.EmployeeID
ORDER BY DeptName, LastName, ProjectNo;

