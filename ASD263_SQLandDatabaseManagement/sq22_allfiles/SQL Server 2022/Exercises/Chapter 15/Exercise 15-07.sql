USE AP;

SELECT v.VendorName, i.InvoiceNumber, i.InvoiceDate, i.InvoiceTotal, dr.Balance
FROM Vendors AS v
  JOIN Invoices AS i
    ON v.VendorID = i.VendorID
  JOIN dbo.fnDateRange('10/10/22','10/20/22') AS dr
    ON i.InvoiceNumber = dr.InvoiceNumber;
