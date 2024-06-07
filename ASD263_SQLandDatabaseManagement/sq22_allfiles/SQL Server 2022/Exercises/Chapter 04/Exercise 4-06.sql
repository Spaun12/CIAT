USE AP;

SELECT DISTINCT v1.VendorID, v1.VendorName,
       v1.VendorContactFName + ' ' + v1.VendorContactLName AS Name
FROM Vendors v1 
   JOIN Vendors v2
      ON (v1.VendorID <> v2.VendorID) AND
      (v1.VendorContactFName = v2.VendorContactFName)
ORDER BY Name;
