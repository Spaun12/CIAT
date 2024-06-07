/*
Log in using your Windows account
before running this script.
*/

USE AP;

ALTER ROLE InvoiceEntry DROP MEMBER MartinRey;
DROP USER MartinRey;
DROP LOGIN MartinRey;