SELECT DATE_BUCKET(MONTH, 1, InvoiceDate) AS Month, 
       SUM(InvoiceTotal) AS Total
FROM Invoices
GROUP BY DATE_BUCKET(MONTH, 1, InvoiceDate);
