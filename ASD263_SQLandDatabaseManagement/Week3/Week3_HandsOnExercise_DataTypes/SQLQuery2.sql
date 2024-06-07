-- Query for Students table
SELECT 
    EnrollmentDate, -- The EnrollmentDate column
    CAST(EnrollmentDate AS DATE) AS EnrollmentDateOnly, -- EnrollmentDate with its date only
    CAST(EnrollmentDate AS TIME) AS EnrollmentTimeOnly, -- EnrollmentDate with its time only
    CONVERT(VARCHAR(5), EnrollmentDate, 1) AS MonthAndDay -- EnrollmentDate with just the month and day
FROM 
    Students;
