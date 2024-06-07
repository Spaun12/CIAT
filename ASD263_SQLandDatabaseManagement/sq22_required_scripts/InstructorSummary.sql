SELECT COUNT(*) AS NumberOfInstructors,
	   MAX(AnnualSalary) AS MaxSalary,
       AVG(AnnualSalary) AS AverageSalary
FROM Instructors;