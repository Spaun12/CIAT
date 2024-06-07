USE AP;

SELECT VendorName, CustLastName, CustFirstName,
    VendorState AS State, VendorCity AS City
FROM AP.dbo.Vendors v
    JOIN ProductOrders.dbo.Customers c
        ON v.VendorZipCode = c.CustZip
ORDER BY State, City;
