USE AP;

DROP FUNCTION IF EXISTS fnTopVendorsDue;
GO

CREATE FUNCTION fnTopVendorsDue
    (@CutOff money = 0)
    RETURNS table
RETURN
	SELECT VendorName, SUM(InvoiceTotal) AS TotalDue
	FROM Vendors v
	  JOIN Invoices i
	    ON v.VendorID = i.VendorID
	WHERE InvoiceTotal - CreditTotal - PaymentTotal > 0
	GROUP BY VendorName
	HAVING SUM(InvoiceTotal) >= @CutOff;
