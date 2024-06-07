USE AP;

SELECT InvoiceNumber, InvoiceDate, InvoiceTotal
FROM Invoices i
  JOIN Vendors v
    ON i.VendorID = v.VendorID
WHERE VendorState = 'CA'
ORDER BY InvoiceDate;

