USE AP;

BEGIN TRY
	UPDATE Invoices
	SET InvoiceDate = NULL
	WHERE InvoiceID = 1;

	PRINT 'Row updated succeeded.'
END TRY
BEGIN CATCH
	PRINT 'Row update failed.';

    PRINT 'Error ' + CONVERT(varchar, ERROR_NUMBER(), 1) 
        + ': ' + ERROR_MESSAGE();
END CATCH;