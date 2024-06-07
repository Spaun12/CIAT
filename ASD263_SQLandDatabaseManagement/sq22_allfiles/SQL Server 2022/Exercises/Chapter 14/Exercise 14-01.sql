USE AP;

DECLARE @InvoiceCount    int;
DECLARE @InvoiceTotalDue decimal;

SELECT @InvoiceCount = COUNT(*), 
	   @InvoiceTotalDue = SUM(InvoiceTotal - PaymentTotal - CreditTotal)
FROM Invoices
WHERE InvoiceTotal - PaymentTotal - CreditTotal > 0;

IF @InvoiceTotalDue  >= 30000
	BEGIN
		PRINT 'Invoice count: ' + CONVERT(varchar, @InvoiceCount);
		PRINT 'Total due:     ' + CONVERT(varchar, @InvoiceTotalDue);
	END
ELSE
	BEGIN
		PRINT 'Total balance due is less than $30,000.';
	END