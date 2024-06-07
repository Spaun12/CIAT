USE AP;

SELECT DISTINCT v1.VendorName, v1.VendorCity, v1.VendorState
FROM Vendors v1 
    JOIN Vendors v2
        ON v1.VendorCity = v2.VendorCity AND
           v1.VendorState = v2.VendorState AND
           v1.VendorID <> v2.VendorID
ORDER BY v1.VendorState, v1.VendorCity;

