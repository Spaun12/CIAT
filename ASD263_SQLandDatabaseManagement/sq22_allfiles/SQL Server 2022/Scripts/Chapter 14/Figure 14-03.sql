USE AP;

DECLARE @MaxInvoice money, 
		@MinInvoice money,
		@InvoiceCount int,
		@PercentDifference decimal(8,2),
		@VendorIDVar int = 95;

SELECT @MaxInvoice = MAX(InvoiceTotal),
       @MinInvoice = MIN(InvoiceTotal), 
       @InvoiceCount = COUNT(*)
FROM Invoices
WHERE VendorID = @VendorIDVar;

SET @PercentDifference = (@MaxInvoice - @MinInvoice) / @MinInvoice * 100;

PRINT 'Maximum invoice is $' + CONVERT(varchar,@MaxInvoice,1) + '.';
PRINT 'Minimum invoice is $' + CONVERT(varchar,@MinInvoice,1) + '.';
PRINT 'Maximum is ' + CONVERT(varchar,@PercentDifference) +
    '% more than minimum.';
PRINT 'Number of invoices: ' + CONVERT(varchar,@InvoiceCount) + '.';
