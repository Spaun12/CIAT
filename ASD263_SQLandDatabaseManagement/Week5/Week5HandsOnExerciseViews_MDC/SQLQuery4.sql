-- Create the view StudentCoursesMin
CREATE VIEW StudentCoursesMin AS
SELECT 
    s.FirstName,
    s.LastName,
    c.CourseNumber,
    c.CourseDescription,
    c.CourseUnits
FROM 
    Students s
JOIN 
    StudentCourses sc ON s.StudentID = sc.StudentID
JOIN 
    Courses c ON sc.CourseID = c.CourseID;
