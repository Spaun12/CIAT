USE AP;

SELECT COUNT(DISTINCT VendorID) AS NumberOfVendors,
    COUNT(VendorID) AS NumberOfInvoices,
    AVG(InvoiceTotal) AS AverageInvoiceAmount,
    SUM(InvoiceTotal) AS TotalInvoiceAmount
FROM Invoices
WHERE InvoiceDate > '2022-07-01';

