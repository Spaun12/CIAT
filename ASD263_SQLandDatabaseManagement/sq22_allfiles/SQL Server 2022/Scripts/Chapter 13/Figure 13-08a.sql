USE AP;

DROP VIEW IF EXISTS IBM_Invoices
GO

CREATE VIEW IBM_Invoices
AS
SELECT InvoiceNumber, InvoiceDate, InvoiceTotal
FROM Invoices
WHERE VendorID = (SELECT VendorID FROM Vendors WHERE VendorName = 'IBM');
