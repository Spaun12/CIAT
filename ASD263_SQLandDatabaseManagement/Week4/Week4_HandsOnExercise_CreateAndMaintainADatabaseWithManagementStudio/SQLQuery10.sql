-- Switch to the MyBookDB database
USE MyBookDB;
GO

-- Add the EmailAddress column to the Users table
ALTER TABLE Users
ADD EmailAddress varchar(255) NOT NULL;
GO

-- Add the BookName column to the Books table
ALTER TABLE Books
ADD BookName varchar(255) NOT NULL;
GO

-- Add the DownloadDate column to the Downloads table
ALTER TABLE Downloads
ADD DownloadDate datetime2 NOT NULL;
GO
