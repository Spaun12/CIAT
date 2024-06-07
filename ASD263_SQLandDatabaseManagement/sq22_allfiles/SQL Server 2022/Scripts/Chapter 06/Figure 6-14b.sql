USE Examples;

WITH EmployeesCTE AS
(
		-- Anchor member
		SELECT EmployeeID, 
			FirstName + ' ' + LastName As EmployeeName, 
			1 As Rank
		FROM Employees
		WHERE ManagerID IS NULL
	UNION ALL
		-- Recursive member
		SELECT e.EmployeeID, 
			FirstName + ' ' + LastName, 
			Rank + 1
		FROM Employees e
			JOIN EmployeesCTE e2
			    ON e.ManagerID = e2.EmployeeID
)
SELECT *
FROM EmployeesCTE
ORDER BY Rank, EmployeeID;