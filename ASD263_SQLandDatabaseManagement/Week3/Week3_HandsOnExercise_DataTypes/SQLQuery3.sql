-- Query for Students table
SELECT 
    EnrollmentDate, -- The EnrollmentDate column
    CONVERT(VARCHAR(8), EnrollmentDate, 1) AS EnrollmentDateMMDDYY, -- EnrollmentDate in MM/DD/YY format
    CONVERT(VARCHAR(20), EnrollmentDate, 100) AS EnrollmentDateMonthDDYYYY, -- EnrollmentDate in Month DD, YYYY format with the hours and minutes on a 12-hour clock with an am/pm indicator
    CONVERT(VARCHAR(5), EnrollmentDate, 108) AS EnrollmentTime24Hour, -- EnrollmentDate with just the time using a 24-hour format
    CONVERT(VARCHAR(5), EnrollmentDate, 1) AS MonthAndDay -- EnrollmentDate with just the month and day
FROM 
    Students;
