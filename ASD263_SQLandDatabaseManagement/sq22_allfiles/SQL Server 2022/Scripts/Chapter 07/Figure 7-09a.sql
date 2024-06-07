USE AP;

DELETE Invoices
WHERE VendorID = 
   (SELECT VendorID
    FROM Vendors 
    WHERE VendorName = 'Blue Cross');
