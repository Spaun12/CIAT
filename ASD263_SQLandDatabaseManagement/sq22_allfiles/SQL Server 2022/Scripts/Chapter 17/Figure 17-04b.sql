/*
   If you change the Windows domain name (Accounting) 
   and the user name (SusanRoberts) to a valid domain name,
   you can use the following statement to alter the Windows login.
*/
-- ALTER LOGIN [Accounting\SusanRoberts] DISABLE;

/*
    Let's alter the SQL Server login instead...
*/
ALTER LOGIN SusanRoberts DISABLE;

