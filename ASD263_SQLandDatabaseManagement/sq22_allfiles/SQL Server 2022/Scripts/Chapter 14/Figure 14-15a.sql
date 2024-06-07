USE AP;

DECLARE @TableNameVar varchar(128) = 'Invoices';

EXEC ('SELECT * FROM ' + @TableNameVar + ';');