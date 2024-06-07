USE AP;

SELECT VendorName, InvoiceNumber AS FirstInv,
       InvoiceDate, InvoiceTotal
FROM Invoices i
  JOIN Vendors v
    ON i.VendorID = v.VendorID
WHERE InvoiceDate =
  (SELECT MIN(InvoiceDate)
   FROM Invoices I_Sub
   WHERE I_Sub.VendorID = i.VendorID)
ORDER BY VendorName;
