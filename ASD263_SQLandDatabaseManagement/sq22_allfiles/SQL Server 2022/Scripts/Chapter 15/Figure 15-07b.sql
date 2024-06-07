USE AP;

BEGIN TRY
    EXEC spInsertInvoice 
         799,'ZXK-799','2023-03-01',299.95,1,'2023-04-01';
END TRY
BEGIN CATCH
    PRINT 'An error occurred.';
    PRINT 'Message: ' + CONVERT(varchar, ERROR_MESSAGE());
    IF ERROR_NUMBER() >= 50000
        PRINT 'This is a custom error message.';
END CATCH;