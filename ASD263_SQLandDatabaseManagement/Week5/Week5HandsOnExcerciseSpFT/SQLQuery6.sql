-- 6a) List all instructors before update
PRINT 'Instructors before update:';
SELECT * FROM Instructors;
GO

-- 6b) Create the trigger Instructors_UPDATE
CREATE TRIGGER Instructors_UPDATE
ON Instructors
AFTER UPDATE
AS
BEGIN
    DECLARE @AnnualSalary MONEY, @InstructorID INT;

    -- Get the new annual salary and instructor ID
    SELECT @AnnualSalary = inserted.AnnualSalary, @InstructorID = inserted.InstructorID
    FROM inserted;

    -- Check if the annual salary is out of bounds
    IF @AnnualSalary < 0 OR @AnnualSalary > 120000
    BEGIN
        RAISERROR('AnnualSalary must be between 0 and 120,000.', 16, 1);
        ROLLBACK TRANSACTION;
        RETURN;
    END

    -- Adjust salary if it's less than 12,000
    IF @AnnualSalary < 12000
    BEGIN
        UPDATE Instructors
        SET AnnualSalary = @AnnualSalary * 12
        WHERE InstructorID = @InstructorID;
    END
END;
GO

-- 6c) Test the trigger with an UPDATE statement
UPDATE Instructors
SET AnnualSalary = 10000
WHERE InstructorID = 1;

-- List all instructors after update
PRINT 'Instructors after update:';
SELECT * FROM Instructors;
GO
