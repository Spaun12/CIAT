USE AP;

DECLARE @TotalInvoiceDue money;

SELECT @TotalInvoiceDue = SUM(InvoiceTotal - CreditTotal - PaymentTotal)
FROM Invoices
WHERE InvoiceTotal - CreditTotal - PaymentTotal > 0;

IF @TotalInvoiceDue > 10000
    SELECT VendorName, InvoiceNumber, InvoiceDueDate,
           InvoiceTotal - CreditTotal - PaymentTotal AS Balance
    FROM Invoices i
      JOIN Vendors v
        ON i.VendorID = v.VendorID
    WHERE InvoiceTotal - CreditTotal - PaymentTotal > 0
    ORDER BY InvoiceDueDate;
ELSE
    PRINT 'Balance due is less than $10,000.00.';
