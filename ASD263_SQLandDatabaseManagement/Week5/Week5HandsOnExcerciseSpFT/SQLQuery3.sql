-- Drop the existing fnStudentUnits function if it exists
IF OBJECT_ID('dbo.fnStudentUnits', 'FN') IS NOT NULL
    DROP FUNCTION dbo.fnStudentUnits;
GO

-- Drop the existing fnTuition function if it exists
IF OBJECT_ID('dbo.fnTuition', 'FN') IS NOT NULL
    DROP FUNCTION dbo.fnTuition;
GO

-- Create the fnStudentUnits function
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

-- Create the fnTuition function
CREATE FUNCTION fnTuition (@StudentID INT)
RETURNS MONEY
AS
BEGIN
    DECLARE @TotalUnits INT;
    DECLARE @Tuition MONEY;
    DECLARE @PartTimeCost MONEY;
    DECLARE @FullTimeCost MONEY;
    DECLARE @PerUnitCost MONEY;

    -- Get the tuition costs
    SELECT 
        @PartTimeCost = PartTimeCost,
        @FullTimeCost = FullTimeCost,
        @PerUnitCost = PerUnitCost
    FROM Tuition;

    -- Get the total units for the student
    SET @TotalUnits = dbo.fnStudentUnits(@StudentID);

    -- Calculate the tuition based on full-time or part-time status
    IF @TotalUnits > 9
        SET @Tuition = @FullTimeCost;
    ELSE
        SET @Tuition = @PartTimeCost + @TotalUnits * @PerUnitCost;

    RETURN @Tuition;
END;
GO
