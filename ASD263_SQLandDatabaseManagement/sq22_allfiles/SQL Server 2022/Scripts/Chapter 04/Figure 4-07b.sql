USE AP;

SELECT VendorName, InvoiceNumber, InvoiceDate,
    InvoiceLineItemAmount AS LineItemAmount, AccountDescription
FROM Vendors AS v, Invoices AS i, InvoiceLineItems AS li, GLAccounts AS gla
WHERE v.VendorID = i.VendorID
   AND i.InvoiceID = li.InvoiceID
   AND li.AccountNo = gla.AccountNo
   AND InvoiceTotal - PaymentTotal - CreditTotal > 0
ORDER BY VendorName, LineItemAmount DESC;
