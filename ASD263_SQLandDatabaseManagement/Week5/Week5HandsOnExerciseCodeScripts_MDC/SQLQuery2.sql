-- Declare variables to hold the count of instructors and the average annual salary
DECLARE @InstructorCount INT;
DECLARE @AvgAnnualSalary MONEY;

-- Set the variables
SELECT 
    @InstructorCount = COUNT(*),
    @AvgAnnualSalary = AVG(AnnualSalary)
FROM Instructors;

-- Display a message based on the count of instructors
IF @InstructorCount >= 10
BEGIN
    PRINT 'The number of instructors is ' + CAST(@InstructorCount AS VARCHAR);
    PRINT 'The average annual salary is ' + CAST(@AvgAnnualSalary AS VARCHAR);
END
ELSE
BEGIN
    PRINT 'The number of fulltime instructors is less than 10';
END;
