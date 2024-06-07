-- Select courses with exactly three units
SELECT 
    LastName,
    FirstName,
    CourseDescription
FROM 
    StudentCoursesMin
WHERE 
    CourseUnits = 3
ORDER BY 
    LastName, FirstName;
