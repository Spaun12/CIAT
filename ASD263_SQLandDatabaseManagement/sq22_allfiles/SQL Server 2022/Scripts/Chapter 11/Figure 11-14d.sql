USE AP;

SELECT name, collation_name 
FROM sys.databases
WHERE name = 'AP';