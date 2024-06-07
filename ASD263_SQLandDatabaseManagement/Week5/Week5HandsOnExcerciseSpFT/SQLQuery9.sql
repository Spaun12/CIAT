-- Drop the existing trigger if it exists
IF OBJECT_ID('dbo.Instructors_UPDATE_Audit', 'TR') IS NOT NULL
    DROP TRIGGER dbo.Instructors_UPDATE_Audit;
GO

-- 8b) Create the trigger Instructors_UPDATE_Audit
CREATE TRIGGER Instructors_UPDATE_Audit
ON Instructors
AFTER UPDATE
AS
BEGIN
    -- Insert old data into InstructorsAudit
    INSERT INTO InstructorsAudit (InstructorID, LastName, FirstName, Status, DepartmentChairman, HireDate, AnnualSalary, DepartmentID, DateUpdated)
    SELECT 
        deleted.InstructorID, 
        deleted.LastName, 
        deleted.FirstName, 
        deleted.Status, 
        deleted.DepartmentChairman, 
        deleted.HireDate, 
        deleted.AnnualSalary, 
        deleted.DepartmentID, 
        GETDATE()
    FROM 
        deleted;
END;
GO
