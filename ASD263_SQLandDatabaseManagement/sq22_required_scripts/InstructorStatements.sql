SELECT LastName, FirstName, HireDate, AnnualSalary
FROM Instructors
ORDER BY AnnualSalary;

SELECT COUNT(*) AS NumberOfInstructors,
	   MAX(AnnualSalary) AS MaxSalary,
       AVG(AnnualSalary) AS AverageSalary
FROM Instructors;