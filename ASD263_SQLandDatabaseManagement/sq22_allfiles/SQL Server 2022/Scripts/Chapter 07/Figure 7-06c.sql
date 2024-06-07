USE AP;

UPDATE Invoices
SET TermsID = 1
WHERE VendorID IN
   (SELECT VendorID
    FROM Vendors
    WHERE VendorState IN ('CA', 'AZ', 'NV'));
