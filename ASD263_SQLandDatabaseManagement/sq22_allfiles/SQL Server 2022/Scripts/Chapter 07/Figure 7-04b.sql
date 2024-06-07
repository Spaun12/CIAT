USE AP;

INSERT INTO InvoiceArchive
    (InvoiceID, VendorID, InvoiceNumber, InvoiceTotal, CreditTotal,
    PaymentTotal, TermsID, InvoiceDate, InvoiceDueDate)
SELECT
    InvoiceID, VendorID, InvoiceNumber, InvoiceTotal, CreditTotal, 
    PaymentTotal, TermsID, InvoiceDate, InvoiceDueDate
FROM Invoices
WHERE InvoiceTotal - PaymentTotal - CreditTotal = 0;
