-- Select the count of students for each course
SELECT 
    CourseID,
    COUNT(StudentID) AS StudentCount
FROM 
    StudentCourses
GROUP BY 
    CourseID
ORDER BY 
    CourseID;
