USE AP;
GO

CREATE PROC spBalanceRange
       @VendorVar varchar(50) = '%',
       @BalanceMin money = 0,
       @BalanceMax money = 0
AS

IF @BalanceMax = 0
  BEGIN
    SELECT VendorName, InvoiceNumber,
           InvoiceTotal - CreditTotal - PaymentTotal AS Balance
    FROM Vendors v 
      JOIN Invoices i
        ON v.VendorID = i.VendorID
    WHERE VendorName LIKE @VendorVar AND
         (InvoiceTotal - CreditTotal - PaymentTotal) > 0 AND
         (InvoiceTotal - CreditTotal - PaymentTotal) >= @BalanceMin
    ORDER BY Balance DESC;
  END;
ELSE
  BEGIN
    SELECT VendorName, InvoiceNumber,
           InvoiceTotal - CreditTotal - PaymentTotal AS Balance
    FROM Vendors v
      JOIN Invoices i
        ON v.VendorID = i.VendorID
    WHERE VendorName LIKE @VendorVar AND
         (InvoiceTotal - CreditTotal - PaymentTotal) > 0 AND
         (InvoiceTotal - CreditTotal - PaymentTotal)
           BETWEEN @BalanceMin AND @BalanceMax
    ORDER BY Balance DESC;
  END;
