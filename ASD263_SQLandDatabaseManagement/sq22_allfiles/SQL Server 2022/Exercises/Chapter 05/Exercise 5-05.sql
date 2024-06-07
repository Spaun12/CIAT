USE AP;

SELECT gl.AccountDescription, COUNT(*) AS LineItemCount,
       SUM(InvoiceLineItemAmount) AS LineItemSum
FROM GLAccounts gl
  JOIN InvoiceLineItems li
    ON gl.AccountNo = li.AccountNo
  JOIN Invoices i
    ON li.InvoiceID = i.InvoiceID
WHERE InvoiceDate BETWEEN '2022-10-01' AND '2022-12-31'
GROUP BY gl.AccountDescription
HAVING COUNT(*) > 1
ORDER BY LineItemCount DESC;
