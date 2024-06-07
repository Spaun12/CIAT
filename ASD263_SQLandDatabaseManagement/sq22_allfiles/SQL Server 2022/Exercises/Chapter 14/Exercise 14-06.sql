USE AP;

DROP TABLE IF EXISTS #InvoiceCopy;

SELECT * INTO #InvoiceCopy FROM Invoices;

WHILE (SELECT COUNT(*) FROM #InvoiceCopy WHERE InvoiceTotal - PaymentTotal - CreditTotal > 100) > 0
	BEGIN
		UPDATE #InvoiceCopy
		SET CreditTotal = CreditTotal + 100 
		WHERE InvoiceTotal - PaymentTotal - CreditTotal > 100;
	END;

SELECT * FROM #InvoiceCopy;