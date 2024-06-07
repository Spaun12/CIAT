USE AP;

SELECT VendorName, InvoiceNumber, InvoiceDate,
       InvoiceTotal - PaymentTotal - CreditTotal AS Balance
FROM Vendors v
JOIN Invoices i
  ON v.VendorID = i.VendorID
WHERE InvoiceTotal - PaymentTotal - CreditTotal > 0
ORDER BY VendorName;
