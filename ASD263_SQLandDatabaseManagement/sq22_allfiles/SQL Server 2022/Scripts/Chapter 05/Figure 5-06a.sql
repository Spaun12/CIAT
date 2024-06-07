USE AP;

SELECT InvoiceDate, COUNT(*) AS InvoiceQty, SUM(InvoiceTotal) AS InvoiceSum
FROM Invoices
GROUP BY InvoiceDate
HAVING InvoiceDate BETWEEN '2023-01-01' AND '2023-01-31'
   AND COUNT(*) > 1
   AND SUM(InvoiceTotal) > 100
ORDER BY InvoiceDate DESC;