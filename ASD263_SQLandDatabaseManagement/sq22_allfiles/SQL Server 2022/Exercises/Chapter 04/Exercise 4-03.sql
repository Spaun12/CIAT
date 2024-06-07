USE AP;

SELECT VendorName, DefaultAccountNo, AccountDescription
FROM Vendors v 
JOIN GLAccounts gl
  ON v.DefaultAccountNo = gl.AccountNo
ORDER BY AccountDescription, VendorName;
