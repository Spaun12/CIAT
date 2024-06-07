USE AP;

UPDATE Invoices
SET TermsID = 2
FROM Invoices i 
  JOIN Vendors v
    ON i.VendorID = v.VendorID
WHERE DefaultTermsID = 2;
