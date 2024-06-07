-- Attempt to delete the department with the name "Sociology"
BEGIN TRY
    -- Attempt to delete the Sociology department
    DELETE FROM Departments
    WHERE DepartmentName = 'Sociology';

    -- If successful, print success message
    PRINT 'SUCCESS: Record was deleted.';
END TRY
BEGIN CATCH
    -- If an error occurs, print failure message and error details
    PRINT 'FAILURE: Record was not deleted.';
    PRINT 'Error ' + CAST(ERROR_NUMBER() AS VARCHAR) + ': ' + ERROR_MESSAGE();
END CATCH;
