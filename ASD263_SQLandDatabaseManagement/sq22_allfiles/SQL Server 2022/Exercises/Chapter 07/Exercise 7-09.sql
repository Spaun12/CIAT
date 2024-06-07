USE AP;

DELETE VendorCopy
WHERE VendorState NOT IN
  (SELECT DISTINCT VendorState
   FROM Vendors v
     JOIN Invoices i
       ON v.VendorID = i.VendorID);
