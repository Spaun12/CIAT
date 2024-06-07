USE AP;

SELECT *
FROM Vendors v
JOIN Invoices i
  ON v.VendorID = i.VendorID;
