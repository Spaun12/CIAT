USE Examples;

SELECT DeptName, d.DeptNo, e.DeptNo, LastName
FROM Departments d
    FULL JOIN Employees e
        ON d.DeptNo = e.DeptNo;

