USE AP;

SELECT gl.AccountDescription, COUNT(*) AS LineItemCount,
       SUM(InvoiceLineItemAmount) AS LineItemSum
FROM GLAccounts gl
  JOIN InvoiceLineItems li
    ON gl.AccountNo = li.AccountNo
GROUP BY gl.AccountDescription
HAVING COUNT(*) > 1
ORDER BY LineItemCount DESC;
