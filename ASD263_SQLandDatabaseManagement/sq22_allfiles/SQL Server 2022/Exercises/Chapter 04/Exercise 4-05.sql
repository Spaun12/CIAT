USE AP;

SELECT VendorName AS Vendor, InvoiceDate AS Date,
       InvoiceNumber AS Number, InvoiceSequence AS [#],
       InvoiceLineItemAmount AS LineItem
FROM Vendors v 
  JOIN Invoices i
    ON v.VendorID = i.VendorID
  JOIN InvoiceLineItems AS li
    ON i.InvoiceID = li.InvoiceID
ORDER BY Vendor, Date, Number, [#];
