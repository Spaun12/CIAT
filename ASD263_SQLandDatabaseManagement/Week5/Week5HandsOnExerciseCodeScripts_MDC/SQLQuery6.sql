-- Declare variables to hold CourseID and the count of students
DECLARE @CourseID INT;
DECLARE @StudentCount INT;

-- Declare a cursor to iterate through courses and their student counts
DECLARE CourseCursor CURSOR FOR
SELECT CourseID, COUNT(StudentID) AS StudentCount
FROM StudentCourses
GROUP BY CourseID;

-- Open the cursor
OPEN CourseCursor;

-- Fetch the first row from the cursor
FETCH NEXT FROM CourseCursor INTO @CourseID, @StudentCount;

-- Loop through the cursor
WHILE @@FETCH_STATUS = 0
BEGIN
    -- Check if there are too few students enrolled
    IF @StudentCount < 5
    BEGIN
        PRINT 'Too few students enrolled in course ' + CAST(@CourseID AS VARCHAR);
    END
    -- Check if there are too many students enrolled
    ELSE IF @StudentCount > 10
    BEGIN
        PRINT 'Too many students enrolled in course ' + CAST(@CourseID AS VARCHAR);
    END

    -- Fetch the next row from the cursor
    FETCH NEXT FROM CourseCursor INTO @CourseID, @StudentCount;
END

-- Close the cursor
CLOSE CourseCursor;

-- Deallocate the cursor
DEALLOCATE CourseCursor;
