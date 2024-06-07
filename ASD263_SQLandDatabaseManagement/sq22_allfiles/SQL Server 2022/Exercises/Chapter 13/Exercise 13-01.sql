CREATE VIEW InvoiceBasic
AS
SELECT VendorName, InvoiceNumber, InvoiceTotal
FROM Vendors v 
  JOIN Invoices i
    ON v.VendorID = i.VendorID;
