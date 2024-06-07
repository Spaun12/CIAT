-- Insert two new instructors with specified details
INSERT INTO Instructors (LastName, FirstName, Status, DepartmentChairman, HireDate, AnnualSalary, DepartmentID)
VALUES ('Benedict', 'Susan', 'P', 0, CONVERT(DATE, GETDATE()), 34000.00, 9),
       ('Adams', NULL, 'F', 1, CONVERT(DATE, GETDATE()), 66000.00, 9);
