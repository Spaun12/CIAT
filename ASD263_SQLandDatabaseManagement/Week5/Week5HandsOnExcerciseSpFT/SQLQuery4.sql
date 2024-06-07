-- List all instructors before insertion
PRINT 'Instructors before insertion:';
SELECT * FROM Instructors;
GO

-- Create the stored procedure spInsertInstructor
CREATE PROCEDURE spInsertInstructor
    @LastName VARCHAR(25),
    @FirstName VARCHAR(25),
    @Status CHAR(1),
    @DepartmentChairman BIT,
    @AnnualSalary MONEY,
    @DepartmentID INT
AS
BEGIN
    -- Check if the annual salary is negative
    IF @AnnualSalary < 0
    BEGIN
        PRINT 'ERROR: AnnualSalary cannot be negative.';
        RETURN;
    END

    -- Insert the new instructor
    INSERT INTO Instructors (LastName, FirstName, Status, DepartmentChairman, AnnualSalary, DepartmentID, HireDate)
    VALUES (@LastName, @FirstName, @Status, @DepartmentChairman, @AnnualSalary, @DepartmentID, GETDATE());

    PRINT 'SUCCESS: Instructor inserted.';
END;
GO

-- Next, test the stored procedure with valid data (should succeed)
EXEC spInsertInstructor 'Doe', 'John', 'F', 0, 60000, 1;

-- List all instructors after successful insertion
PRINT 'Instructors after successful insertion:';
SELECT * FROM Instructors;
GO

-- Test the stored procedure with invalid data (should fail)
EXEC spInsertInstructor 'Doe', 'Jane', 'F', 0, -50000, 1;

-- List all instructors after failed insertion
PRINT 'Instructors after failed insertion:';
SELECT * FROM Instructors;
GO

