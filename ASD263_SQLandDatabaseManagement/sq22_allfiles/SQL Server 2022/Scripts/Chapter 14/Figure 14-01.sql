/*
Creates three tables in a database named ClubRoster.
*/

CREATE DATABASE ClubRoster;
GO

USE ClubRoster;

CREATE TABLE Members
(MemberID int NOT NULL IDENTITY PRIMARY KEY,
LastName varchar(75) NOT NULL,
FirstName varchar(50) NOT NULL,
MiddleName varchar(50) NULL);

CREATE TABLE Committees
(CommitteeID int NOT NULL IDENTITY PRIMARY KEY,
CommitteeName varchar(50) NOT NULL);

CREATE TABLE CommitteeAssignments
(MemberID int NOT NULL REFERENCES Members(MemberID),
CommitteeID int NOT NULL REFERENCES Committees(CommitteeID));