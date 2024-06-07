USE AP;

UPDATE Invoices
SET CreditTotal = CreditTotal + 100
WHERE InvoiceNumber = '97/522';
