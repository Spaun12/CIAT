-- 8a) Create the InstructorsAudit table
CREATE TABLE InstructorsAudit (
    AuditID INT IDENTITY PRIMARY KEY,
    InstructorID INT,
    LastName VARCHAR(25),
    FirstName VARCHAR(25),
    Status CHAR(1),
    DepartmentChairman BIT,
    HireDate DATE,
    AnnualSalary MONEY,
    DepartmentID INT,
    DateUpdated DATETIME2
);
GO

-- Let's verify that the table was created
SELECT * FROM InstructorsAudit;
GO
