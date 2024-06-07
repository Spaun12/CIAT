SELECT TOP 10 VendorName, SUM(InvoiceTotal) AS Total
FROM Invoices i
  JOIN Vendors v
    ON i.VendorID = v.VendorID
GROUP BY VendorName
ORDER BY Total DESC
