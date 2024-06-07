USE AP;

DROP TABLE IF EXISTS #FirstInvoice;

SELECT VendorID, MIN(InvoiceDate) AS FirstInvoiceDate
INTO #FirstInvoice
FROM Invoices
GROUP BY VendorID;

SELECT VendorName, FirstInvoiceDate, InvoiceTotal
FROM Invoices i
  JOIN #FirstInvoice fi
    ON i.VendorID = fi.VendorID 
	AND i.InvoiceDate = fi.FirstInvoiceDate
  JOIN Vendors v
    ON i.VendorID = v.VendorID
ORDER BY VendorName, FirstInvoiceDate;
