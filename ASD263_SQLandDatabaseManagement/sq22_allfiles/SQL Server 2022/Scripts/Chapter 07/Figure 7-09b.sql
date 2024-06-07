USE AP;

DELETE Invoices
FROM Invoices i
  JOIN Vendors v
    ON i.VendorID = v.VendorID
WHERE VendorName = 'Blue Cross';
