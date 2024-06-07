USE AP;

SELECT TOP 1 VendorID, AVG(InvoiceTotal) AS AvgInvoice
INTO #TopVendors
FROM Invoices
GROUP BY VendorID
ORDER BY AvgInvoice DESC;

SELECT i.VendorID, MAX(InvoiceDate) AS LatestInv
FROM Invoices AS i JOIN #TopVendors AS tv
    ON i.VendorID = tv.VendorID
GROUP BY i.VendorID;