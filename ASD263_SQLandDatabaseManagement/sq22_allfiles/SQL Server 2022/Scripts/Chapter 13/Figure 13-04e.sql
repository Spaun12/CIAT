USE AP;
GO

CREATE VIEW InvoiceSummary
AS
SELECT VendorName, COUNT(*) AS InvoiceQty, SUM(InvoiceTotal) AS InvoiceSum
FROM Vendors AS v JOIN Invoices AS i ON v.VendorID = i.VendorID
GROUP BY VendorName;
