USE Membership;

ALTER TABLE Individuals
ADD DuesPaid bit NOT NULL DEFAULT 0;
