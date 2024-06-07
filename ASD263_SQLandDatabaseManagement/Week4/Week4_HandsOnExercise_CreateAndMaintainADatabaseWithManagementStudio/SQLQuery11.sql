-- Drop the MyWebDB database if it already exists
IF EXISTS (SELECT name FROM sys.databases WHERE name = 'MyWebDB')
DROP DATABASE MyWebDB
GO

-- Create the MyWebDB database
CREATE DATABASE MyWebDB
GO

-- Use the MyWebDB database
USE MyWebDB
GO

-- Create the Users table
CREATE TABLE Users (
    UserID int IDENTITY(1,1) PRIMARY KEY,
    EmailAddress varchar(255) UNIQUE NOT NULL,
    FirstName varchar(255),
    LastName varchar(255) NOT NULL
)
GO

-- Create the Products table
CREATE TABLE Products (
    ProductID int IDENTITY(1,1) PRIMARY KEY,
    ProductName varchar(255) UNIQUE NOT NULL
)
GO

-- Create the Downloads table
CREATE TABLE Downloads (
    DownloadID int IDENTITY(1,1) PRIMARY KEY,
    UserID int FOREIGN KEY REFERENCES Users(UserID),
    ProductID int FOREIGN KEY REFERENCES Products(ProductID),
    FileName varchar(255),
    DownloadDate datetime2
)
GO

-- Check if the Users table has been created
SELECT * FROM Users;

-- Check if the Downloads table has been created
SELECT * FROM Downloads;

-- Check if the Products table has been created
SELECT * FROM Products;
