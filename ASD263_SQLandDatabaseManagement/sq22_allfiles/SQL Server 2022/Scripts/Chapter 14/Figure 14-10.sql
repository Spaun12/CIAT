USE AP;

DECLARE @InvoiceIDVar int, 
        @InvoiceTotalVar money, 
		@UpdateCount int = 0;

DECLARE Invoices_Cursor CURSOR
FOR
    SELECT InvoiceID, InvoiceTotal  FROM Invoices
    WHERE InvoiceTotal - PaymentTotal - CreditTotal > 0;

OPEN Invoices_Cursor;

FETCH NEXT FROM Invoices_Cursor INTO @InvoiceIDVar, @InvoiceTotalVar;
WHILE @@FETCH_STATUS <> -1
    BEGIN
        IF @InvoiceTotalVar > 1000
        BEGIN
            UPDATE Invoices
            SET CreditTotal = CreditTotal + (InvoiceTotal * .1)
            WHERE InvoiceID = @InvoiceIDVar;

            SET @UpdateCount = @UpdateCount + 1;
        END;
        FETCH NEXT FROM Invoices_Cursor INTO @InvoiceIDVar, @InvoiceTotalVar;
    END;

CLOSE Invoices_Cursor;
DEALLOCATE Invoices_Cursor;
    
PRINT '';
PRINT CONVERT(varchar, @UpdateCount) + ' row(s) updated.';