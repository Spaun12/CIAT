USE AP;

SELECT VendorState, VendorCity, COUNT(*) AS InvoiceQty,
    AVG(InvoiceTotal) AS InvoiceAvg
FROM Invoices i 
  JOIN Vendors v
    ON i.VendorID = v.VendorID
GROUP BY VendorState, VendorCity
ORDER BY VendorState, VendorCity;

