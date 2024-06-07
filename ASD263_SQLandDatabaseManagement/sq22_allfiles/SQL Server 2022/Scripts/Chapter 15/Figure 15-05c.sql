USE AP;

DECLARE @MyInvTotal money;
EXEC spInvTotal3 
    @DateVar = '2023-01-01', 
	@VendorVar = 'P%',
    @InvTotal = @MyInvTotal OUTPUT;

PRINT '$' + CONVERT(varchar,@MyInvTotal,1);