USE AP;

    SELECT InvoiceNumber, VendorName, '33% Payment' AS PaymentType,
           InvoiceTotal AS Total, InvoiceTotal * 0.333 AS Payment
    FROM Invoices i
        JOIN Vendors v
            ON i.VendorID = v.VendorID
    WHERE InvoiceTotal > 10000
UNION
    SELECT InvoiceNumber, VendorName, '50% Payment' AS PaymentType,
           InvoiceTotal AS Total, InvoiceTotal * 0.5 AS Payment
    FROM Invoices i
        JOIN Vendors v
            ON i.VendorID = v.VendorID
    WHERE InvoiceTotal BETWEEN 500 AND 10000
UNION
    SELECT InvoiceNumber, VendorName, 'Full amount' AS PaymentType,
           InvoiceTotal AS Total, InvoiceTotal AS Payment
    FROM Invoices i
        JOIN Vendors v
            ON i.VendorID = v.VendorID
    WHERE InvoiceTotal < 500
ORDER BY PaymentType, VendorName, InvoiceNumber;


