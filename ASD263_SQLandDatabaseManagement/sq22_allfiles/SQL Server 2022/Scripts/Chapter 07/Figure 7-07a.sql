USE AP;

UPDATE Invoices
SET TermsID = 1
FROM Invoices i 
  JOIN Vendors v
    ON i.VendorID = v.VendorID
WHERE VendorName = 'Pacific Bell';
