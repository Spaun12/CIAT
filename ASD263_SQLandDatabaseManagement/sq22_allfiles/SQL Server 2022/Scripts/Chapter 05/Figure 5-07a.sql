USE AP;

SELECT VendorID, COUNT(*) AS InvoiceCount,
    SUM(InvoiceTotal) AS InvoiceTotal
FROM Invoices
GROUP BY ROLLUP(VendorID);
