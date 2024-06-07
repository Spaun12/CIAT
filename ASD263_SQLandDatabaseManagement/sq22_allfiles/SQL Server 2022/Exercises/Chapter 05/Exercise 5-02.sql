USE AP;

SELECT TOP 10 VendorName, SUM(PaymentTotal) AS PaymentSum
FROM Vendors v 
  JOIN Invoices i
    ON v.VendorID = i.VendorID
GROUP BY VendorName
ORDER BY PaymentSum DESC;
