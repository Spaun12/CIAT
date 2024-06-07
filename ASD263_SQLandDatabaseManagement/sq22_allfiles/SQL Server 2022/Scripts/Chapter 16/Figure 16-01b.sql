USE AP;

BEGIN TRY
    BEGIN TRAN;
        INSERT Invoices
        VALUES (34,'ZXA-080','2023-03-01',14092.59,0,0,3,'2023-03-31',NULL);

        DECLARE @InvoiceID int = @@IDENTITY;

        INSERT InvoiceLineItems VALUES (@InvoiceID,1,160,4447.23,'HW upgrade');
        INSERT InvoiceLineItems VALUES (@InvoiceID,2,167,9645.36,'OS upgrade');
    COMMIT TRAN;
END TRY
BEGIN CATCH
    ROLLBACK TRAN;
END CATCH;