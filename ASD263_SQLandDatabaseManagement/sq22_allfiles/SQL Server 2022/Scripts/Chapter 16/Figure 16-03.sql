USE AP;

BEGIN TRAN;
PRINT 'BEGIN Tran Count: ' + CONVERT(varchar, @@TRANCOUNT);
DELETE Invoices;
  BEGIN TRAN;
    PRINT 'BEGIN Tran Count: ' + CONVERT(varchar, @@TRANCOUNT);
    DELETE Vendors;
  COMMIT TRAN;          -- This COMMIT decrements @@TRANCOUNT.
                        -- It doesn't commit 'DELETE Vendors'.
  PRINT 'COMMIT   Tran Count: ' + CONVERT(varchar, @@TRANCOUNT);
ROLLBACK TRAN;
PRINT 'ROLLBACK Tran Count: ' + CONVERT(varchar, @@TRANCOUNT);

PRINT ' ';

DECLARE @VendorsCount int = (SELECT COUNT(*) FROM Vendors);
DECLARE @InvoicesCount int = (SELECT COUNT(*) FROM Invoices);
PRINT 'Vendors Count:  ' + CONVERT(varchar, @VendorsCount);
PRINT 'Invoices Count: ' + CONVERT(varchar, @InvoicesCount);