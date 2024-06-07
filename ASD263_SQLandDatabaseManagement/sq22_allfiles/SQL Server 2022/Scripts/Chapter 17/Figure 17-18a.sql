/*
Log in using your Windows account 
before running this script.
*/

USE AP;

-- drop MartinRey login/user if it exists
DROP USER IF EXISTS MartinRey;

IF EXISTS (SELECT * FROM sys.server_principals 
           WHERE name = 'MartinRey')
    DROP LOGIN MartinRey;

-- create MartinRey login/user
CREATE LOGIN MartinRey WITH PASSWORD = 'Martin$Rey',
	DEFAULT_DATABASE = AP;

CREATE USER MartinRey;

-- add MartinRey to the InvoiceEntry role
ALTER ROLE InvoiceEntry ADD MEMBER MartinRey;