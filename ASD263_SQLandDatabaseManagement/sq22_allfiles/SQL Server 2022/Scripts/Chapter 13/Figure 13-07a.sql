USE AP;

DROP VIEW IF EXISTS VendorPayment;
GO

CREATE VIEW VendorPayment
AS
SELECT VendorName, InvoiceNumber, InvoiceDate, PaymentDate,
    InvoiceTotal, CreditTotal, PaymentTotal
FROM Invoices i
  JOIN Vendors v 
    ON i.VendorID = v.VendorID
WHERE InvoiceTotal - PaymentTotal - CreditTotal > 0;
