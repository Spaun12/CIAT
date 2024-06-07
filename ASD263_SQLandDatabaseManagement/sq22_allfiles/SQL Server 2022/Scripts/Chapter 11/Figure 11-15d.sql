USE Payroll;

ALTER TABLE Employees
ALTER COLUMN EmployeeName VARCHAR(200)
                          COLLATE Latin1_General_100_CI_AS_SC_UTF8;