USE AP;

SELECT v.VendorName, VendorCity, TotalDue
FROM Vendors v
  JOIN dbo.fnTopVendorsDue(DEFAULT) t
    ON v.VendorName = t.VendorName;