USE AP;

DROP TABLE IF EXISTS #InvoiceCopy;

SELECT * INTO #InvoiceCopy FROM Invoices;

UPDATE #InvoiceCopy
SET CreditTotal = CreditTotal + 100 
WHERE InvoiceTotal - PaymentTotal - CreditTotal > 100;

SELECT * FROM #InvoiceCopy;