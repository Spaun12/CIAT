-- Select the top 5 students with the most units using TOP
SELECT TOP 5
    LastName,
    FirstName,
    UnitsTotal
FROM 
    StudentCoursesSummary
ORDER BY 
    UnitsTotal DESC;
