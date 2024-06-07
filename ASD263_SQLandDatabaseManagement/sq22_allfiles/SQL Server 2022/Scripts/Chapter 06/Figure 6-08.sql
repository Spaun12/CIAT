USE AP;

SELECT VendorID, VendorName, VendorState
FROM Vendors v
WHERE NOT EXISTS
    (SELECT *
    FROM Invoices i
    WHERE i.VendorID = v.VendorID);

