USE AP;

DROP PROC IF EXISTS spCopyInvoices;

GO

CREATE PROC spCopyInvoices
AS
    DROP TABLE IF EXISTS InvoiceCopy;

    SELECT *
    INTO InvoiceCopy
    FROM Invoices;