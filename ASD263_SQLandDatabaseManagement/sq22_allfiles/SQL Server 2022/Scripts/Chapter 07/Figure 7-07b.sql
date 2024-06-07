USE AP;

UPDATE Vendors
SET VendorContactLName = LastName,
    VendorContactFName = FirstName
FROM Vendors v
JOIN ContactUpdates c
    ON v.VendorID = c.VendorID;
