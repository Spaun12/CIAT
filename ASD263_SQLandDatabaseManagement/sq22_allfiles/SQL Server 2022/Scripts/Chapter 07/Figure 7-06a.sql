USE AP;

UPDATE Invoices
SET CreditTotal = CreditTotal + 100,
    InvoiceDueDate = (SELECT MAX(InvoiceDueDate) FROM Invoices)
WHERE InvoiceNumber = '97/522';
