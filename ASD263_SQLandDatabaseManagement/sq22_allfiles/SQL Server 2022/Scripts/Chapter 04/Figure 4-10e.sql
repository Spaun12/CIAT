USE Examples;

SELECT DeptName, LastName, ProjectNo
FROM Departments d
    FULL JOIN Employees e
        ON d.DeptNo = e.DeptNo
    FULL JOIN Projects p
        ON e.EmployeeID = p.EmployeeID
ORDER BY DeptName;
