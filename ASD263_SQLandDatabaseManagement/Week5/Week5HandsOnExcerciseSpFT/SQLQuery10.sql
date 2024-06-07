-- 8c) List all audit records before update
PRINT 'InstructorsAudit before update:';
SELECT * FROM InstructorsAudit;
GO

-- Test the trigger with an UPDATE statement
UPDATE Instructors
SET AnnualSalary = 80000
WHERE InstructorID = 1;
GO

-- List all audit records after update
PRINT 'InstructorsAudit after update:';
SELECT * FROM InstructorsAudit;
GO
