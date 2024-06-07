USE AP;

SELECT i.VendorID, MAX(InvoiceDate) AS LatestInv,
    AVG(InvoiceTotal) AS AvgInvoice
FROM Invoices i
    JOIN
        (SELECT TOP 5 VendorID, AVG(InvoiceTotal) AS AvgInvoice
        FROM Invoices
        GROUP BY VendorID
        ORDER BY AvgInvoice DESC) tv -- tv for TopVendor
            ON i.VendorID = tv.VendorID
GROUP BY i.VendorID
ORDER BY LatestInv DESC;

