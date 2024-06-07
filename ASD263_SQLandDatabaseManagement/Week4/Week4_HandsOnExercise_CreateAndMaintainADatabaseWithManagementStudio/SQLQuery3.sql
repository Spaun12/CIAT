-- Set the UserID column in the Downloads table as a foreign key
ALTER TABLE Downloads
ADD CONSTRAINT FK_Downloads_Users FOREIGN KEY (UserID) REFERENCES Users(UserID);
GO

-- Set the BookID column in the Downloads table as a foreign key
ALTER TABLE Downloads
ADD CONSTRAINT FK_Downloads_Books FOREIGN KEY (BookID) REFERENCES Books(BookID);
GO
