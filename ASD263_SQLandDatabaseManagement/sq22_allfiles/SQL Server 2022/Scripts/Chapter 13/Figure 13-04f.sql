USE AP;
GO

CREATE VIEW VendorsDue
WITH SCHEMABINDING
AS
SELECT InvoiceDate AS Date, VendorName AS Name,
    VendorContactFName + ' ' + VendorContactLName AS Contact,
    InvoiceNumber AS Invoice,
    InvoiceTotal - PaymentTotal - CreditTotal AS BalanceDue
FROM dbo.Vendors AS v JOIN dbo.Invoices AS i
    ON v.VendorID = i.VendorID
WHERE InvoiceTotal - PaymentTotal - CreditTotal > 0;
