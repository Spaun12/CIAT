/*
Handles insertion of new invoices into AP database,
including data validation.
Author:         Bryan Syverson
Created:        2002-07-17
Modified:       2008-07-29 by Joel Murach
                2020-01-31 by Anne Boehm
                2023-01-30 by Scott McCoy
Return value:   InvoiceID for the new row if successful, 
                0 if unsuccessful
*/
USE AP;
GO

DROP PROC IF EXISTS spInsertInvoice;
GO

CREATE PROC spInsertInvoice
       @VendorID       int = NULL,
       @InvoiceNumber  varchar(50) = NULL,
       @InvoiceDate    date = NULL,
       @InvoiceTotal   money = NULL,
       @PaymentTotal   money = NULL,
       @CreditTotal    money = NULL,
       @TermsID        int = NULL,
       @InvoiceDueDate date = NULL,
       @PaymentDate    date = NULL
AS

IF NOT EXISTS (SELECT * FROM Vendors WHERE VendorID = @VendorID)
    THROW 50001, 'Invalid VendorID.', 1;
IF @InvoiceNumber IS NULL
    THROW 50001, 'Invalid InvoiceNumber.', 1;
IF @InvoiceDate IS NULL 
OR @InvoiceDate > GETDATE() 
OR DATEDIFF(dd, @InvoiceDate, GETDATE()) > 30
    THROW 50001, 'Invalid InvoiceDate.', 1;
IF @InvoiceTotal IS NULL 
OR @InvoiceTotal <= 0
    THROW 50001, 'Invalid InvoiceTotal.', 1;
IF @PaymentTotal IS NULL
    SET @PaymentTotal = 0;
IF @CreditTotal IS NULL
    SET @CreditTotal = 0;
IF @CreditTotal > @InvoiceTotal
    THROW 50001, 'Invalid CreditTotal.', 1;
IF @PaymentTotal > @InvoiceTotal - @CreditTotal
    THROW 50001, 'Invalid PaymentTotal.', 1;
IF NOT EXISTS (SELECT * FROM Terms WHERE TermsID = @TermsID)
    IF @TermsID IS NULL
        SELECT @TermsID = DefaultTermsID
        FROM Vendors
        WHERE VendorID = @VendorID;
    ELSE  -- @TermsID IS NOT NULL
        THROW 50001, 'Invalid TermsID.', 1;
IF @InvoiceDueDate IS NULL
	BEGIN
	  DECLARE @TermsDueDays int = (SELECT TermsDueDays 
								   FROM Terms 
								   WHERE TermsID = @TermsID);

	  SET @InvoiceDueDate = DATEADD(day, @TermsDueDays, @InvoiceDate);
	END
ELSE  -- @InvoiceDueDate IS NOT NULL
    IF @InvoiceDueDate < @InvoiceDate OR
            DATEDIFF(dd, @InvoiceDueDate, @InvoiceDate) > 180
        THROW 50001, 'Invalid InvoiceDueDate.', 1;
IF @PaymentDate < @InvoiceDate OR
        DATEDIFF(dd, @PaymentDate, GETDATE()) > 14
    THROW 50001, 'Invalid PaymentDate.', 1;

INSERT Invoices
VALUES (@VendorID, @InvoiceNumber, @InvoiceDate, @InvoiceTotal,
        @PaymentTotal, @CreditTotal, @TermsID, @InvoiceDueDate, 
        @PaymentDate);
RETURN @@IDENTITY;