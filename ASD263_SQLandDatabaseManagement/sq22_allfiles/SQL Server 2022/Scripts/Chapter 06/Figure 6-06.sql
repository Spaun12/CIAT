USE AP;

SELECT VendorName, InvoiceNumber, InvoiceTotal
FROM Vendors v
  JOIN Invoices i
    ON v.VendorID = i.VendorID
WHERE InvoiceTotal < ANY
    (SELECT InvoiceTotal
    FROM Invoices
    WHERE VendorID = 115);


