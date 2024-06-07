USE AP;

/*
   If you change the Windows domain name (Accounting) 
   and the user name (SusanRoberts) to a valid domain name,
   you can use the following statement to create the user.
*/
-- CREATE USER SusanRoberts FOR LOGIN [Accounting\SusanRoberts];

/*
    Let's create a normal SQL Server user instead...
*/
CREATE USER SusanRoberts;
