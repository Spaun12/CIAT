-- 5a) List all instructors before update
PRINT 'Instructors before update:';
SELECT * FROM Instructors;
GO

-- 5b) Create the stored procedure spUpdateInstructor
CREATE PROCEDURE spUpdateInstructor
    @InstructorID INT,
    @AnnualSalary MONEY
AS
BEGIN
    -- Check if the annual salary is negative
    IF @AnnualSalary < 0
    BEGIN
        PRINT 'ERROR: AnnualSalary must be a positive number.';
        RETURN;
    END

    -- Update the instructor's annual salary
    UPDATE Instructors
    SET AnnualSalary = @AnnualSalary
    WHERE InstructorID = @InstructorID;

    PRINT 'SUCCESS: Instructor salary updated.';
END;
GO

-- Test the stored procedure with valid data (should succeed)
EXEC spUpdateInstructor 1, 70000;

-- 5c) List all instructors after successful update
PRINT 'Instructors after successful update:';
SELECT * FROM Instructors;
GO

-- Test the stored procedure with invalid data (should fail)
EXEC spUpdateInstructor 1, -10000;

-- 5d)List all instructors after failed update
PRINT 'Instructors after failed update:';
SELECT * FROM Instructors;
GO
