USE AP;

SELECT DISTINCT VendorName,
    (SELECT MAX(InvoiceDate) FROM Invoices i
    WHERE i.VendorID = v.VendorID) AS LatestInv
FROM Vendors v
ORDER BY LatestInv DESC;

