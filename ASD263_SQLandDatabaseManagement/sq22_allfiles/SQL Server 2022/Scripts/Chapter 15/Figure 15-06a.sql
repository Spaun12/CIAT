USE AP;

DROP PROC IF EXISTS spInvCount;
GO

CREATE PROC spInvCount
       @DateVar date = NULL,
       @VendorVar varchar(40) = '%'
AS

IF @DateVar IS NULL
   SELECT @DateVar = MIN(InvoiceDate) FROM Invoices;

DECLARE @InvCount int;

SELECT @InvCount = COUNT(InvoiceID)
FROM Invoices i
  JOIN Vendors v
    ON i.VendorID = v.VendorID
WHERE (InvoiceDate >= @DateVar) AND
       (VendorName LIKE @VendorVar);

RETURN @InvCount;