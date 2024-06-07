USE AP;

WITH Summary AS
(
    SELECT VendorState, VendorName, SUM(InvoiceTotal) AS SumOfInvoices
    FROM Invoices i
      JOIN Vendors v
        ON i.VendorID = v.VendorID
    GROUP BY VendorState, VendorName
),

TopInState AS
(
    SELECT VendorState, MAX(SumOfInvoices) AS SumOfInvoices
    FROM Summary
    GROUP BY VendorState
)

SELECT s.VendorState, s.VendorName, t.SumOfInvoices
FROM Summary s 
    JOIN TopInState t
        ON s.VendorState = t.VendorState AND
           s.SumOfInvoices = t.SumOfInvoices
ORDER BY s.VendorState;