-- Switch to the MyBookDB database
USE MyBookDB;
GO

-- Create an index on the UserID foreign key in the Downloads table
CREATE INDEX IDX_Downloads_UserID ON Downloads(UserID);
GO

-- Create an index on the BookID foreign key in the Downloads table
CREATE INDEX IDX_Downloads_BookID ON Downloads(BookID);
GO

-- Verify the indexes in the Downloads table
EXEC sp_helpindex 'Downloads';
