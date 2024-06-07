-- Create BookDatabase
CREATE DATABASE BookDatabase;
GO

-- Use BookDatabase for the following operations
USE BookDatabase;
GO

-- Create Users table
CREATE TABLE Users (
    UserID INT PRIMARY KEY,
    EmailAddress VARCHAR(255),
    FirstName VARCHAR(255),
    LastName VARCHAR(255)
);
GO

-- Create Books table
CREATE TABLE Books (
    BookID INT PRIMARY KEY,
    BookName VARCHAR(255)
);
GO

-- Create Downloads table
CREATE TABLE Downloads (
    DownloadID INT PRIMARY KEY,
    UserID INT FOREIGN KEY REFERENCES Users(UserID),
    BookID INT FOREIGN KEY REFERENCES Books(BookID),
    FileName VARCHAR(255),
    DownloadDateTime DATETIME
);
GO
