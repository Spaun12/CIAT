/*
   To get the following script to run correctly,
   you must change the Windows domain name (Accounting) to the correct domain name, 
   and you must change the user name (SusanRoberts) to the login ID for that domain name.
*/
-- CREATE LOGIN [Accounting\SusanRoberts] FROM WINDOWS;

/*
   Let's create a SQL Server Login named SusanRoberts instead...
*/
CREATE LOGIN SusanRoberts WITH PASSWORD = 'az2950ZQ!Y';