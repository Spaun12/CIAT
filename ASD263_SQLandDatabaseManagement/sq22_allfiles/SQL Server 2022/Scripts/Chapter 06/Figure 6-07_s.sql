USE AP;

-- The subquery
SELECT AVG(InvoiceTotal)
FROM Invoices i_sub
WHERE i_sub.VendorID = 95;
