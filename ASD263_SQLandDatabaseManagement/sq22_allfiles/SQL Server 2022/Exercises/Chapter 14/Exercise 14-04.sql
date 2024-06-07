USE AP;

DROP VIEW IF EXISTS FirstInvoiceView;
GO

CREATE VIEW FirstInvoiceView
AS
SELECT VendorID, MIN(InvoiceDate) AS FirstInvoiceDate
FROM Invoices
GROUP BY VendorID;
GO

SELECT VendorName, FirstInvoiceDate, InvoiceTotal
FROM Invoices i 
  JOIN FirstInvoiceView fi
    ON i.VendorID = fi.VendorID 
	AND i.InvoiceDate = fi.FirstInvoiceDate
  JOIN Vendors v
    ON i.VendorID = v.VendorID
ORDER BY VendorName, FirstInvoiceDate;