USE AP;

SELECT InvoiceNumber, TermsID
FROM Invoices
WHERE TermsID IN (1, 3, 4);