USE AP;
GO

DROP VIEW IF EXISTS IBM_Invoices
GO

CREATE VIEW IBM_Invoices
AS
SELECT InvoiceNumber, InvoiceDate, InvoiceTotal
FROM Invoices
WHERE VendorID = (SELECT VendorID FROM Vendors WHERE VendorName = 'IBM');
GO

DROP TRIGGER IF EXISTS IBM_Invoices_INSERT;
GO

CREATE TRIGGER IBM_Invoices_INSERT
    ON IBM_Invoices
    INSTEAD OF INSERT
AS
DECLARE @InvoiceDate date,      @InvoiceNumber varchar(50),
        @InvoiceTotal money,    @VendorID int,
        @InvoiceDueDate date,   @TermsID int,
        @DefaultDays smallint,  @RowCount int;


SELECT @RowCount = COUNT(*) FROM Inserted;

IF @RowCount = 1
    BEGIN
        SELECT @InvoiceNumber = InvoiceNumber, 
		       @InvoiceDate = InvoiceDate,
			   @InvoiceTotal = InvoiceTotal
        FROM Inserted;

        IF (@InvoiceDate IS NOT NULL AND 
		    @InvoiceNumber IS NOT NULL AND
            @InvoiceTotal IS NOT NULL)
            BEGIN
                SELECT @VendorID = VendorID, 
				       @TermsID = DefaultTermsID
                FROM Vendors 
                WHERE VendorName = 'IBM';

                SELECT @DefaultDays = TermsDueDays
                FROM Terms
                WHERE TermsID = @TermsID;

                SET @InvoiceDueDate =
					DATEADD(day, @DefaultDays, @InvoiceDate);

                INSERT Invoices (VendorID, InvoiceNumber, InvoiceDate,
                    InvoiceTotal, TermsID, InvoiceDueDate, PaymentDate)
                VALUES (@VendorID, @InvoiceNumber, @InvoiceDate,
                   @InvoiceTotal, @TermsID, @InvoiceDueDate, NULL);
            END;
    END;
ELSE
	THROW 50027, 'Limit INSERT to a single row.', 1;
