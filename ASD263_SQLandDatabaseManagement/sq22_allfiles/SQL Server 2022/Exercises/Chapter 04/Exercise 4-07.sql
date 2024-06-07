USE AP;

SELECT gl.AccountNo, AccountDescription
FROM GLAccounts gl
LEFT JOIN InvoiceLineItems li
  ON gl.AccountNo = li.AccountNo
WHERE li.AccountNo IS NULL
ORDER BY gl.AccountNo;
