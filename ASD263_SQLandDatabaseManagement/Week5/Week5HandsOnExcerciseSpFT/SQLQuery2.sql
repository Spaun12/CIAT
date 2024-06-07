-- Creating the function fnStudentUnits
CREATE FUNCTION fnStudentUnits (@StudentID INT)
RETURNS INT
AS
BEGIN
    DECLARE @TotalUnits INT;

    -- Calculate the total units for the student
    SELECT @TotalUnits = SUM(C.CourseUnits)
    FROM StudentCourses SC
    JOIN Courses C ON SC.CourseID = C.CourseID
    WHERE SC.StudentID = @StudentID;

    RETURN @TotalUnits;
END;
GO

-- Testing if the function 
-- with a SELECT statement works
SELECT 
    SC.StudentID, 
    C.CourseNumber, 
    C.CourseUnits, 
    dbo.fnStudentUnits(SC.StudentID) AS TotalUnits
FROM 
    StudentCourses SC
JOIN 
    Courses C ON SC.CourseID = C.CourseID;
