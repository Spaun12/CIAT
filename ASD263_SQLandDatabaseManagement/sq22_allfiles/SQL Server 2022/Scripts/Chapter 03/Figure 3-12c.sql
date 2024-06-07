USE AP;

-- The subquery
SELECT VendorID
     FROM Invoices
     WHERE InvoiceDate = '2022-12-01';

-- The query
SELECT VendorID, InvoiceNumber, InvoiceDate
FROM Invoices
WHERE VendorID IN
    (SELECT VendorID
     FROM Invoices
     WHERE InvoiceDate = '2022-12-01');