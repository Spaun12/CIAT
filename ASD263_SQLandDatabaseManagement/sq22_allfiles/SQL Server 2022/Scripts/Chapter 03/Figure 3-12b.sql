USE AP;

SELECT VendorName, VendorState
FROM Vendors
WHERE VendorState NOT IN ('CA', 'NV', 'OR');