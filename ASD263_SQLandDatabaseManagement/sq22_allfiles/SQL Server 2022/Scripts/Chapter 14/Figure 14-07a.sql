USE AP;

DECLARE @EarliestInvoiceDue date;

SELECT @EarliestInvoiceDue = MIN(InvoiceDueDate)
FROM Invoices
WHERE InvoiceTotal - PaymentTotal - CreditTotal > 0;

IF @EarliestInvoiceDue < GETDATE()
    PRINT 'Outstanding invoices overdue!';