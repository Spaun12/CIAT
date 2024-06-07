USE AP;

DROP TRIGGER IF EXISTS Invoices_UPDATE;
GO

CREATE TRIGGER Invoices_UPDATE
    ON Invoices
    AFTER UPDATE
AS
IF EXISTS           --Test whether PaymentTotal was changed
 (SELECT *
  FROM Deleted d
    JOIN Invoices i
      ON d.InvoiceID = i.InvoiceID
  WHERE d.PaymentTotal <> i.PaymentTotal)
  BEGIN
    IF EXISTS       --Test whether line items total and InvoiceTotal match
     (SELECT *
      FROM Invoices i 
      JOIN
          (SELECT InvoiceID, SUM(InvoiceLineItemAmount) AS SumOfInvoices
           FROM InvoiceLineItems
           GROUP BY InvoiceID) AS li
        ON i.InvoiceID = li.InvoiceID
      WHERE (i.InvoiceTotal <> li.SumOfInvoices) AND
            (li.InvoiceID IN (SELECT InvoiceID FROM Deleted)))
      BEGIN
        THROW 50113, 'Correct line item amounts before posting payment.', 1;
        ROLLBACK TRAN;
      END;
  END;