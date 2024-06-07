-- Switch to the newly created database
USE MyBookDB;
GO

-- Create the Users table with UserID as primary key and identity column
CREATE TABLE Users (
    UserID int IDENTITY(1,1) PRIMARY KEY NOT NULL
);

-- Verify the Users table creation
SELECT * FROM Users;

-- Create the Books table with BookID as primary key and identity column
CREATE TABLE Books (
    BookID int IDENTITY(1,1) PRIMARY KEY NOT NULL
);

-- Verify the Books table creation
SELECT * FROM Books;

-- Create the Downloads table with DownloadID as primary key and identity column
CREATE TABLE Downloads (
    DownloadID int IDENTITY(1,1) PRIMARY KEY NOT NULL,
    UserID int NOT NULL,
    BookID int NOT NULL
);

-- Verify the Downloads table creation
SELECT * FROM Downloads;
