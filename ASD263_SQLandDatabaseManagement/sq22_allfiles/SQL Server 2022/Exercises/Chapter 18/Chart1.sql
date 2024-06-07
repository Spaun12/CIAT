SELECT InvoiceDate, SUM(InvoiceTotal) AS Total
FROM Invoices
GROUP BY InvoiceDate