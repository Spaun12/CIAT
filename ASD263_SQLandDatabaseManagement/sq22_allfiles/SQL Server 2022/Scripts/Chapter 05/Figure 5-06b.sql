USE AP;

SELECT InvoiceDate, COUNT(*) AS InvoiceQty, SUM(InvoiceTotal) AS InvoiceSum
FROM Invoices
WHERE InvoiceDate BETWEEN '2023-01-01' AND '2023-01-31'
GROUP BY InvoiceDate
HAVING COUNT(*) > 1
   AND SUM(InvoiceTotal) > 100
ORDER BY InvoiceDate DESC;
