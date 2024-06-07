-- Switch to the MyBookDB database
USE MyBookDB;
GO

-- Index for EmailAddress
CREATE UNIQUE INDEX IDX_Users_EmailAddress ON Users(EmailAddress);
GO

-- Index for BookName
CREATE UNIQUE INDEX IDX_Books_BookName ON Books(BookName);
GO

-- Index for DownloadDate
CREATE INDEX IDX_Downloads_DownloadDate ON Downloads(DownloadDate);
GO

-- Verify the indexes in the Users table
EXEC sp_helpindex 'Users';

-- Verify the indexes in the Books table
EXEC sp_helpindex 'Books';

-- Verify the indexes in the Downloads table
EXEC sp_helpindex 'Downloads';
