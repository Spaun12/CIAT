USE AP;
GO

CREATE VIEW VendorInvoices
AS
SELECT VendorName, InvoiceNumber, InvoiceDate, InvoiceTotal 
FROM Vendors AS v JOIN Invoices AS i ON v.VendorID = i.VendorID;