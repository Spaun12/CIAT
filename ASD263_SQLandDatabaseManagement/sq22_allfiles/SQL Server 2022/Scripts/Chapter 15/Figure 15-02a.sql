USE AP;

DROP PROC IF EXISTS spInvoiceReport;
GO

CREATE PROC spInvoiceReport
AS

SELECT VendorName, InvoiceNumber, InvoiceDate, InvoiceTotal
FROM Invoices i
  JOIN Vendors v
    ON i.VendorID = v.VendorID
WHERE InvoiceTotal - CreditTotal - PaymentTotal > 0
ORDER BY VendorName;
