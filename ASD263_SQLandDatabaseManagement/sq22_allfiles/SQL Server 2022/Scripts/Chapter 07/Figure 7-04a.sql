USE AP;

INSERT INTO InvoiceArchive
SELECT *
FROM Invoices
WHERE InvoiceTotal - PaymentTotal - CreditTotal = 0;
