USE AP;

DROP PROC IF EXISTS spInvTotal2;
GO

CREATE PROC spInvTotal2
       @DateVar date = NULL
AS
IF @DateVar IS NULL
    SELECT @DateVar = MIN(InvoiceDate) FROM Invoices;

SELECT SUM(InvoiceTotal)
FROM Invoices
WHERE InvoiceDate >= @DateVar;