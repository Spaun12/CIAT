USE AP;
GO

CREATE VIEW StateTotals
AS 
SELECT VendorState, SUM(InvoiceTotal) AS InvoiceTotal
FROM Invoices i JOIN Vendors v ON i.VendorID = v.VendorID
GROUP BY VendorState;