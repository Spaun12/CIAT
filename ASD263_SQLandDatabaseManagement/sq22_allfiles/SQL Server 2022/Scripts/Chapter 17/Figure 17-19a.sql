/*
Be sure you log in using your Windows account
before running this script.
*/

USE AP;

IF  EXISTS (SELECT * FROM sys.database_principals 
            WHERE name = 'AppInvoiceQuery' AND type = 'A')
     DROP APPLICATION ROLE AppInvoiceQuery;

CREATE APPLICATION ROLE AppInvoiceQuery
	WITH PASSWORD = 'AppQry2720';

GRANT SELECT
ON Invoices
TO AppInvoiceQuery;

IF  EXISTS (SELECT * FROM sys.database_principals 
            WHERE name = 'TestAppRole')
   DROP USER TestAppRole;
IF  EXISTS (SELECT * FROM sys.server_principals 
            WHERE name = 'TestAppRole')
    DROP LOGIN TestAppRole;

CREATE LOGIN TestAppRole WITH PASSWORD = 'App$Role1',
	DEFAULT_DATABASE = AP;
CREATE USER TestAppRole;

/*
Afterward, login as TestAppRole 
before running Figure 17-19b.sql. 
*/