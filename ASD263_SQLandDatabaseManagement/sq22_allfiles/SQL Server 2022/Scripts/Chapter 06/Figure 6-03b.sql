USE AP;

SELECT v.VendorID, VendorName, VendorState
FROM Vendors v
  LEFT JOIN Invoices i
    ON v.VendorID = i.VendorID
WHERE i.VendorID IS NULL;
