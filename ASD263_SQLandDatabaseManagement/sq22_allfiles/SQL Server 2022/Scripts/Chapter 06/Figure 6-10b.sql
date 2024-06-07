USE AP;

SELECT VendorName, MAX(InvoiceDate) AS LatestInv
FROM Vendors v
    LEFT JOIN Invoices i
        ON v.VendorID = i.VendorID
GROUP BY VendorName
ORDER BY LatestInv DESC;
