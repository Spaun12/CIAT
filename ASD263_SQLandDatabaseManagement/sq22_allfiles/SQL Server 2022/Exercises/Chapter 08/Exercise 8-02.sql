USE AP;

SELECT CAST(InvoiceDate AS varchar) AS CastAsVarchar,
       TRY_CONVERT(varchar,InvoiceDate,1) AS ConvertToStyle1,
       TRY_CONVERT(varchar,InvoiceDate,10) AS ConvertToStyle10
FROM Invoices;
