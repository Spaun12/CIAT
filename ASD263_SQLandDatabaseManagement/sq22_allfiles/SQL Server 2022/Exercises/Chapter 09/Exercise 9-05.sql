USE AP;

SELECT 
    VendorID, 
    DATE_BUCKET(WEEK, 1, InvoiceDate, CAST('2022-11-06' AS DATE)) AS WeekEnding, 
    SUM(InvoiceTotal) AS InvoiceTotal
FROM Invoices
GROUP BY VendorID, DATE_BUCKET(WEEK, 1, InvoiceDate, CAST('2022-11-06' AS DATE))
ORDER BY VendorID, WeekEnding