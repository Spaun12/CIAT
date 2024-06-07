USE AP;
GO

DROP PROC IF EXISTS spInsertInvoice;
GO

CREATE PROC spInsertInvoice
       @VendorID    int,  @InvoiceNumber  varchar(50),
       @InvoiceDate date, @InvoiceTotal   money,
       @TermsID     int,  @InvoiceDueDate date
AS

IF EXISTS(SELECT * FROM Vendors WHERE VendorID = @VendorID)
    INSERT Invoices
    VALUES (@VendorID, @InvoiceNumber,
            @InvoiceDate, @InvoiceTotal, 0, 0,
            @TermsID, @InvoiceDueDate, NULL);
ELSE 
    THROW 50001, 'Not a valid VendorID!', 1;