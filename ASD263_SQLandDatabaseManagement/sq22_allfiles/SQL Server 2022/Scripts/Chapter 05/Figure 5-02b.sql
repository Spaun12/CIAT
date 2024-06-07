USE AP;

SELECT 'After 7/1/2022' AS SelectionDate, COUNT(*) AS NumberOfInvoices,
    MAX(InvoiceTotal) AS HighestInvoiceTotal,
    MIN(InvoiceTotal) AS LowestInvoiceTotal
FROM Invoices
WHERE InvoiceDate > '2022-07-01';
