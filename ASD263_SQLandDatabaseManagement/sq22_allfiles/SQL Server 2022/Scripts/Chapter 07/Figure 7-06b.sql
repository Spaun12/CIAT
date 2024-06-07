USE AP;

UPDATE Invoices
SET TermsID = 1
WHERE VendorID =
   (SELECT VendorID
    FROM Vendors
    WHERE VendorName = 'Pacific Bell');
