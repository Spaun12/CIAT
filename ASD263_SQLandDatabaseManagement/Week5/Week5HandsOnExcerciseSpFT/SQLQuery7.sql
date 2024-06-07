-- 7A)List all instructors before insert
PRINT 'Instructors before insert:';
SELECT * FROM Instructors;
GO

-- Create the trigger Instructors_INSERT
CREATE TRIGGER Instructors_INSERT
ON Instructors
AFTER INSERT
AS
BEGIN
    -- Update HireDate if it is NULL
    UPDATE Instructors
    SET HireDate = GETDATE()
    WHERE HireDate IS NULL;
END;
GO

-- Test the trigger with an INSERT statement
INSERT INTO Instructors (LastName, FirstName, Status, DepartmentChairman, AnnualSalary, DepartmentID)
VALUES ('Smith', 'Alice', 'P', 0, 50000, 2);

-- List all instructors after insert
PRINT 'Instructors after insert:';
SELECT * FROM Instructors;
GO
