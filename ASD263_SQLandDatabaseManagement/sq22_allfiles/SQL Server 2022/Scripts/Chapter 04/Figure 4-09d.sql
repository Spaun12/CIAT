USE Examples;

SELECT DeptName, e.DeptNo, LastName
FROM Departments d 
    RIGHT JOIN Employees e
        ON d.DeptNo = e.DeptNo;
