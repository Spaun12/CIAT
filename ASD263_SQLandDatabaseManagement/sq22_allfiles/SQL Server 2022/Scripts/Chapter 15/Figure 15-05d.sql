USE AP;

DECLARE @MyInvTotal money;
EXEC spInvTotal3 
    @VendorVar = 'P%', 
	@InvTotal = @MyInvTotal OUTPUT;

PRINT '$' + CONVERT(varchar,@MyInvTotal,1);