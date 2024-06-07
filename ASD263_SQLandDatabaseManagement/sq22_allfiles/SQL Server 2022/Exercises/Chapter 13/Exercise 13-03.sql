CREATE VIEW Top10PaidInvoices
AS
SELECT TOP 10 VendorName,
       MAX(InvoiceDate) AS LastInvoice,
       SUM(InvoiceTotal) AS SumOfInvoices
FROM Vendors v
  JOIN Invoices i
    ON v.VendorID = i.VendorID
WHERE InvoiceTotal - CreditTotal - PaymentTotal = 0
GROUP BY VendorName
ORDER BY SUM(InvoiceTotal) DESC;
