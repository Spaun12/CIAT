-- Switch to the MyBookDB database
USE MyBookDB;
GO

-- Alter the Users table to ensure that UserID does not allow null values
ALTER TABLE Users
ALTER COLUMN UserID int NOT NULL;
GO

-- Alter the Books table to ensure that BookID does not allow null values
ALTER TABLE Books
ALTER COLUMN BookID int NOT NULL;
GO

-- Alter the Downloads table to ensure that DownloadID does not allow null values
ALTER TABLE Downloads
ALTER COLUMN DownloadID int NOT NULL;
GO

-- Alter the Downloads table to ensure that UserID does not allow null values
ALTER TABLE Downloads
ALTER COLUMN UserID int NOT NULL;
GO

-- Alter the Downloads table to ensure that BookID does not allow null values
ALTER TABLE Downloads
ALTER COLUMN BookID int NOT NULL;
GO
