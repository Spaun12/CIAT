USE AP;

-- The TopInState subquery
SELECT Summary2.VendorState, MAX(Summary2.SumOfInvoices) AS SumOfInvoices
FROM
    (SELECT v.VendorState, v.VendorName, 
            SUM(i.InvoiceTotal) AS SumOfInvoices
     FROM Invoices AS i JOIN Vendors AS v ON i.VendorID = v.VendorID
     GROUP BY v.VendorState, v.VendorName) AS Summary2
GROUP BY Summary2.VendorState;