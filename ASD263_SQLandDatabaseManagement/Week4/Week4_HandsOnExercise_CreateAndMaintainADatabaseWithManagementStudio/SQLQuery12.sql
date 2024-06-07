-- Add two rows to the Users table
INSERT INTO Users (EmailAddress, FirstName, LastName)
VALUES ('user1@example.com', 'User', 'One'), ('user2@example.com', 'User', 'Two')

-- Add two rows to the Products table
INSERT INTO Products (ProductName)
VALUES ('Product One'), ('Product Two')

-- Add three rows to the Downloads table
INSERT INTO Downloads (UserID, ProductID, FileName, DownloadDate)
VALUES (1, 1, 'file1.txt', GETDATE()), (2, 1, 'file2.txt', GETDATE()), (2, 2, 'file3.txt', GETDATE())
GO

-- Check the data in the Users table
SELECT * FROM Users;

-- Check the data in the Downloads table
SELECT * FROM Downloads;

-- Check the data in the Products table
SELECT * FROM Products;

