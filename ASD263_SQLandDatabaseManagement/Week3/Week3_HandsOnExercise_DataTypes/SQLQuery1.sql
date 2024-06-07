-- Query for Instructors table
SELECT 
    AnnualSalary/12 AS MonthlySalary, -- The monthly salary
    CAST(AnnualSalary/12 AS DECIMAL(10,1)) AS MonthlySalaryDecimal, -- Monthly salary with 1 digit to the right of the decimal point
    CONVERT(INT, AnnualSalary/12) AS MonthlySalaryInteger, -- Monthly salary as an integer using CONVERT
    CAST(AnnualSalary/12 AS INT) AS MonthlySalaryIntegerCast -- Monthly salary as an integer using CAST
FROM 
    Instructors;
