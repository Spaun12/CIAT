-- Make sure to select the AP database before running this query

SELECT *
FROM Vendors
WHERE VendorState = 'CA'
ORDER BY VendorID;