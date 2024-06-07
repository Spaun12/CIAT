-- Create the view StudentCoursesSummary
CREATE VIEW StudentCoursesSummary AS
SELECT 
    s.LastName,
    s.FirstName,
    COUNT(c.CourseID) AS CourseCount,
    SUM(c.CourseUnits) AS UnitsTotal
FROM 
    Students s
JOIN 
    StudentCourses sc ON s.StudentID = sc.StudentID
JOIN 
    Courses c ON sc.CourseID = c.CourseID
GROUP BY 
    s.LastName, s.FirstName
HAVING 
    SUM(c.CourseUnits) > 9;
