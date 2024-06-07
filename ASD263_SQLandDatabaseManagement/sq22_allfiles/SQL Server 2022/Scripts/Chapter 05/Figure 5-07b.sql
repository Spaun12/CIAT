USE AP;

SELECT VendorState, VendorCity, COUNT(*) AS QtyVendors
FROM Vendors
WHERE VendorState IN ('IA', 'NJ')
GROUP BY ROLLUP(VendorState, VendorCity)
ORDER BY VendorState DESC, VendorCity DESC;

