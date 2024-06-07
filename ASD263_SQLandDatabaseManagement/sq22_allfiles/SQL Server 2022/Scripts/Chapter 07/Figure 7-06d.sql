USE AP;

UPDATE Invoices
SET CreditTotal = CreditTotal + 100
FROM
   (SELECT TOP 3 InvoiceID
    FROM Invoices
    WHERE InvoiceTotal - PaymentTotal - CreditTotal >= 100
    ORDER BY InvoiceTotal - PaymentTotal - CreditTotal DESC) AS TopInvoices
WHERE Invoices.InvoiceID = TopInvoices.InvoiceID;
