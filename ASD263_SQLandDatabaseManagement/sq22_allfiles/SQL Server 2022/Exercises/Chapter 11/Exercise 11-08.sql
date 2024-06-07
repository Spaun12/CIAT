USE Membership;

ALTER TABLE Groups
ALTER COLUMN GroupName VARCHAR(200)
                       COLLATE Latin1_General_100_CI_AS_SC_UTF8;
