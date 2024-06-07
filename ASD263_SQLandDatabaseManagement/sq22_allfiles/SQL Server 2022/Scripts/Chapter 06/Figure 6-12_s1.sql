USE AP;

-- The Summary subquery
SELECT v.VendorState, v.VendorName, 
       SUM(i.InvoiceTotal) AS SumOfInvoices
FROM Invoices AS i JOIN Vendors AS v ON i.VendorID = v.VendorID
GROUP BY v.VendorState, v.VendorName;