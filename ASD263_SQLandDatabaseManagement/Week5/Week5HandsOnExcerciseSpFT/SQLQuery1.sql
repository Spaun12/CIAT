-- List all departments before insertion
PRINT 'Departments before insertion:';
SELECT * FROM Departments;
GO

-- Create the stored procedure spInsertDepartment
CREATE PROCEDURE spInsertDepartment
    @DepartmentName VARCHAR(40)
AS
BEGIN
    BEGIN TRY
        -- Attempt to insert a new department
        INSERT INTO Departments (DepartmentName)
        VALUES (@DepartmentName);
        PRINT 'SUCCESS: Department inserted.';
    END TRY
    BEGIN CATCH
        -- Handle any errors
        PRINT 'FAILURE: Could not insert department.';
        PRINT 'Error ' + CAST(ERROR_NUMBER() AS VARCHAR) + ': ' + ERROR_MESSAGE();
    END CATCH;
END;
GO

-- Test the stored procedure with a unique department name (should succeed)
EXEC spInsertDepartment 'History';

-- List all departments after successful insertion
PRINT 'Departments after successful insertion:';
SELECT * FROM Departments;
GO

-- Test the stored procedure with a duplicate department name for the cap stone (should fail)
EXEC spInsertDepartment 'History';
