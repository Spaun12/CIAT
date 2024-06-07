USE AP;

DELETE Invoices
FROM Invoices i
  JOIN 
       (SELECT VendorID, SUM(InvoiceTotal) AS TotalOfInvoices
        FROM Invoices
        GROUP BY VendorID) AS s
    ON i.VendorID = s.VendorID
WHERE TotalOfInvoices <= 100;