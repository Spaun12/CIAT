USE AP;
GO

CREATE VIEW OutstandingInvoices 
    (InvoiceNumber, InvoiceDate, InvoiceTotal, BalanceDue)
AS
SELECT InvoiceNumber, InvoiceDate, InvoiceTotal,
    InvoiceTotal - PaymentTotal - CreditTotal
FROM Invoices
WHERE InvoiceTotal - PaymentTotal - CreditTotal > 0;
