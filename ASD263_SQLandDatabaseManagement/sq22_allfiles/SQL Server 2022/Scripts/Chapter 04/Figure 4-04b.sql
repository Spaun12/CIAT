USE AP;

SELECT InvoiceNumber, InvoiceDate,
    InvoiceTotal, InvoiceLineItemAmount
FROM Invoices i
    JOIN InvoiceLineItems li
        ON i.InvoiceID = li.InvoiceID
WHERE i.InvoiceTotal > li.InvoiceLineItemAmount
ORDER BY InvoiceNumber;

