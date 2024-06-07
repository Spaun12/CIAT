USE AP;

SELECT InvoiceNumber, VendorName
FROM Vendors v, Invoices i
WHERE v.VendorID = i.VendorID;


