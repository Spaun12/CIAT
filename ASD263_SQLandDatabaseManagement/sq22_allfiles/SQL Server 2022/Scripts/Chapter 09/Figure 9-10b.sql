USE AP;

SELECT DATE_BUCKET(MONTH, 1, InvoiceDate) AS Month, 
    SUM(InvoiceTotal) AS InvoiceTotal,
    AVG(InvoiceTotal) AS InvoiceAverage
FROM Invoices
GROUP BY DATE_BUCKET(MONTH, 1, InvoiceDate);
