USE AP;

DROP PROC IF EXISTS spInvTotal3;
GO

CREATE PROC spInvTotal3
       @InvTotal money OUTPUT,
       @DateVar date = NULL,
       @VendorVar varchar(40) = '%'
AS

IF @DateVar IS NULL
   SELECT @DateVar = MIN(InvoiceDate) FROM Invoices;

SELECT @InvTotal = SUM(InvoiceTotal)
FROM Invoices i
  JOIN Vendors v
    ON i.VendorID = v.VendorID
WHERE InvoiceDate >= @DateVar
  AND VendorName LIKE @VendorVar;