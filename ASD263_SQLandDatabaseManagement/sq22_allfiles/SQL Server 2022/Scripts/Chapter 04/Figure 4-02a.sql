USE AP;

SELECT InvoiceNumber, VendorName, InvoiceDueDate,
    InvoiceTotal - PaymentTotal - CreditTotal AS BalanceDue
FROM Vendors 
    JOIN Invoices
        ON Vendors.VendorID = Invoices.VendorID
WHERE InvoiceTotal - PaymentTotal - CreditTotal > 0
ORDER BY InvoiceDueDate DESC;
