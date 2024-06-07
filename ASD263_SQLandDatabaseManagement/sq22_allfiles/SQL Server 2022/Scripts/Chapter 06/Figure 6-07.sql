USE AP;

SELECT VendorID, InvoiceNumber, InvoiceTotal
FROM Invoices i
WHERE InvoiceTotal >
    (SELECT AVG(InvoiceTotal)
    FROM Invoices AS i_sub
    WHERE i_sub.VendorID = i.VendorID)
ORDER BY VendorID, InvoiceTotal;

