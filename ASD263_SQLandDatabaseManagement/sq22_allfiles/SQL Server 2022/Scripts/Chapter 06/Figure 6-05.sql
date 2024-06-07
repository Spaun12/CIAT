USE AP;

SELECT VendorName, InvoiceNumber, InvoiceTotal
FROM Invoices i
  JOIN Vendors v
    ON i.VendorID = v.VendorID
WHERE InvoiceTotal > ALL
    (SELECT InvoiceTotal
    FROM Invoices
    WHERE VendorID = 34)
ORDER BY VendorName;

