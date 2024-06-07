USE AP;

DROP PROC IF EXISTS spInvTotal1;
GO

CREATE PROC spInvTotal1
       @DateVar date,
       @InvTotal money OUTPUT
AS
SELECT @InvTotal = SUM(InvoiceTotal)
FROM Invoices
WHERE InvoiceDate >= @DateVar;