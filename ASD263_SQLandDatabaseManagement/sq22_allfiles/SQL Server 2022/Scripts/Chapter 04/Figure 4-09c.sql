USE Examples;

SELECT DeptName, d.DeptNo, LastName
FROM Departments d
    LEFT JOIN Employees e
        ON d.DeptNo = e.DeptNo;
