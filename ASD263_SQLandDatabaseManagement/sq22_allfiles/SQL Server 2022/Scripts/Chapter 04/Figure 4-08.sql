USE AP;

SELECT VendorName, InvoiceNumber, InvoiceTotal
FROM Vendors v
    LEFT JOIN Invoices i
        ON v.VendorID = i.VendorID
ORDER BY VendorName;

