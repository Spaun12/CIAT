USE AP;
GO

CREATE FUNCTION fnDateRange
      (@DateMin date, @DateMax date)
RETURNS table

RETURN
(SELECT InvoiceNumber, InvoiceDate, InvoiceTotal,
        InvoiceTotal - CreditTotal - PaymentTotal AS Balance
 FROM Invoices
 WHERE InvoiceDate BETWEEN @DateMin AND @DateMax);
