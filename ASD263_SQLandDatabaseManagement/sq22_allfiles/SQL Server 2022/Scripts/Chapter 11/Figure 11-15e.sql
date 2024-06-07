USE Payroll;

INSERT INTO Employees
VALUES (1, 'Murach, Joel');

INSERT INTO Employees
VALUES (2, 'Boehm, Anne');

INSERT INTO Employees
VALUES (3, 'Taylor, Judy');

INSERT INTO Employees
VALUES (4, 'Baylon, Juliette');

SELECT * FROM Employees
ORDER BY EmployeeName COLLATE Latin1_General_100_BIN2;