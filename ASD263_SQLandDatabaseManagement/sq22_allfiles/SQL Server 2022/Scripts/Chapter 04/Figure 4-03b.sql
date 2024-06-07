USE AP;

SELECT VendorName, CustLastName, CustFirstName,
    VendorState AS State, VendorCity AS City
FROM Vendors v
    JOIN ProductOrders..Customers c
        ON v.VendorZipCode = c.CustZip
ORDER BY State, City;
