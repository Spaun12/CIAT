USE AP;

BEGIN TRAN;
  INSERT InvoiceArchive
  SELECT *
  FROM Invoices
  WHERE InvoiceTotal - CreditTotal - PaymentTotal = 0 
    AND InvoiceID NOT IN (SELECT InvoiceID FROM InvoiceArchive);

  DELETE Invoices
  WHERE InvoiceID IN (SELECT InvoiceID FROM InvoiceArchive);

COMMIT TRAN;