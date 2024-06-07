USE AP;

SELECT VendorName, InvoiceNumber, InvoiceDueDate,
       InvoiceTotal - CreditTotal - PaymentTotal AS Balance
FROM Vendors v 
  JOIN Invoices i
    ON v.VendorID = i.VendorID
WHERE InvoiceID = dbo.fnUnpaidInvoiceID();
