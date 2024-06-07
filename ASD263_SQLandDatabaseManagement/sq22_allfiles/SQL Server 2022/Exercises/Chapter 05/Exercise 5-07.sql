USE AP;

SELECT VendorName, AccountDescription, COUNT(*) AS LineItemCount,
       SUM(InvoiceLineItemAmount) AS LineItemSum
FROM Vendors v 
  JOIN Invoices i
   ON v.VendorID = i.VendorID
 JOIN InvoiceLineItems li
   ON i.InvoiceID = li.InvoiceID
 JOIN GLAccounts gl
   ON li.AccountNo = gl.AccountNo
GROUP BY VendorName, AccountDescription
ORDER BY VendorName, AccountDescription;
