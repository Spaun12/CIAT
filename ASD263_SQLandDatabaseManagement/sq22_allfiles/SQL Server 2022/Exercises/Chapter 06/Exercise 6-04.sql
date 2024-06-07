USE AP;

SELECT AccountNo, AccountDescription
FROM GLAccounts gl
WHERE NOT EXISTS
    (SELECT *
     FROM InvoiceLineItems li
     WHERE li.AccountNo = gl.AccountNo)
ORDER BY AccountNo;
