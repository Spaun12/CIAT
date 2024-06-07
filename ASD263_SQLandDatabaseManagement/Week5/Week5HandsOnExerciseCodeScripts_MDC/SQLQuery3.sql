-- Create a temporary table for part-time instructors hired in 2020
CREATE TABLE #TempInstructors (
    InstructorID INT,
    LastName VARCHAR(25),
    FirstName VARCHAR(25),
    Status CHAR(1),
    DepartmentChairman BIT,
    HireDate DATE,
    AnnualSalary MONEY,
    DepartmentID INT
);

-- Insert data into the temporary table
INSERT INTO #TempInstructors
SELECT * 
FROM Instructors
WHERE Status = 'P' AND YEAR(HireDate) = 2020;

-- Declare a variable to hold the average annual salary
DECLARE @AvgAnnualSalary MONEY;

-- Loop to adjust salaries
WHILE (SELECT AVG(AnnualSalary) FROM #TempInstructors) < 40000
BEGIN
    UPDATE #TempInstructors
    SET AnnualSalary = AnnualSalary + 50
    WHERE AnnualSalary < 41000;
END;

-- Select the updated data
SELECT FirstName, LastName, AnnualSalary
FROM #TempInstructors;

-- Drop the temporary table
DROP TABLE #TempInstructors;
