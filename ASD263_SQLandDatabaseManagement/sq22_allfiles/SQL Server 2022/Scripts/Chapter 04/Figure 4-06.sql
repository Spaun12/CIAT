USE AP;

SELECT VendorName, InvoiceNumber, InvoiceDate,
    InvoiceLineItemAmount AS LineItemAmount, AccountDescription
FROM Vendors v
    JOIN Invoices i 
        ON v.VendorID = i.VendorID
    JOIN InvoiceLineItems li 
        ON i.InvoiceID = li.InvoiceID
    JOIN GLAccounts gla 
        ON li.AccountNo = gla.AccountNo
WHERE InvoiceTotal - PaymentTotal - CreditTotal > 0
ORDER BY VendorName, LineItemAmount DESC;
