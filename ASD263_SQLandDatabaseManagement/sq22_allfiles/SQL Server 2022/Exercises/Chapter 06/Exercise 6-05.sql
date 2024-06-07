USE AP;

SELECT VendorName, i.InvoiceID, InvoiceSequence, InvoiceLineItemAmount
FROM Vendors v
  JOIN Invoices i
    ON v.VendorID = i.VendorID
  JOIN InvoiceLineItems li
    ON i.InvoiceID = li.InvoiceID
WHERE i.InvoiceID IN
      (SELECT InvoiceID
       FROM InvoiceLineItems
       WHERE InvoiceSequence > 1)
ORDER BY VendorName, i.InvoiceID, InvoiceSequence;
