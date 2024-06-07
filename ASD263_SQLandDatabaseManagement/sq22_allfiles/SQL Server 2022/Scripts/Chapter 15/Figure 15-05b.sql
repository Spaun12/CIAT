USE AP;

DECLARE @MyInvTotal money;
EXEC spInvTotal3 @MyInvTotal OUTPUT, '2023-01-01', 'P%';

PRINT '$' + CONVERT(varchar,@MyInvTotal,1);