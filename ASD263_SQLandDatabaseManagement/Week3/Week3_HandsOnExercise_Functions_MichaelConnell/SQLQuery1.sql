-- 1) For the Instructors table: Selecting AnnualSalary, MonthlySalary and MonthlySalaryRounded from Instructors table
-- My Thoughts: Rounding to 2 decimal places makes it much easier to view, would be nice if it were a default when using Salary in the query itself.
SELECT 
    AnnualSalary, 
    AnnualSalary / 12 AS MonthlySalary, 
    ROUND((AnnualSalary / 12), 2) AS MonthlySalaryRounded 
FROM 
    Instructors;

-- 2) For the Students table: Selecting EnrollmentDate, Year, Day and EnrollmentDatePlusFour from Students table
-- My Thoughts: I can see where this would help view other patterns such as how students enroll at the beginning vs the end of the month.

SELECT 
    EnrollmentDate, 
    YEAR(EnrollmentDate) AS Year, 
    DAY(EnrollmentDate) AS Day, 
    CAST(DATEADD(YEAR, 4, EnrollmentDate) AS CHAR(4)) AS EnrollmentDatePlusFour 
FROM 
    Students;

-- 3) For each course: Selecting DepartmentName, CourseNumber, FirstName, LastName and ConcatenatedColumn from Departments, Courses and Instructors tables
-- My Thoughts: This concatenated column could be a unique identifier for each course which I find very useful.
SELECT 
    D.DepartmentName, 
    C.CourseNumber, 
    I.FirstName, 
    I.LastName, 
    CONCAT(UPPER(SUBSTRING(D.DepartmentName, 1, 3)), CAST(C.CourseNumber AS CHAR), COALESCE(LEFT(I.FirstName, 1), ''), I.LastName) AS ConcatenatedColumn 
FROM 
    Departments D, Courses C, Instructors I 
WHERE 
    C.DepartmentID = D.DepartmentID AND 
    C.InstructorID = I.InstructorID;

-- 4) For the Students table: Selecting FirstName, LastName, EnrollmentDate, GraduationDate and MonthsBetween from Students table
-- My Thoughts: The number of months between enrollment and graduation would likely be a decent indicator of student success I bet.
SELECT 
    FirstName, 
    LastName, 
    EnrollmentDate, 
    GraduationDate, 
    DATEDIFF(MONTH, EnrollmentDate, GraduationDate) AS MonthsBetween 
FROM 
    Students 
WHERE 
    GraduationDate IS NOT NULL;

-- 5) For each student who has at least one course:Creating a CTE that returns StudentID and CourseUnits
-- My Thoughts: Took a bit of tweaking, but it seems to work now. Very Useful.
WITH StudentCourseUnits AS (
    SELECT 
        S.StudentID, 
        SUM(C.CourseUnits) AS CourseUnits 
    FROM 
        dbo.Students S 
    JOIN 
        dbo.StudentCourses SC ON S.StudentID = SC.StudentID 
    JOIN 
        dbo.Courses C ON SC.CourseID = C.CourseID 
    GROUP BY 
        S.StudentID
)
-- Selecting StudentID, CourseUnits, FulltimeOrParttime and TotalTuition from StudentCourseUnits and Tuition tables
-- My Thoughts: The total tuition cost is potentialy a complex calculation, Best to keep things simple and correct.
SELECT 
    SCU.StudentID, 
    SCU.CourseUnits, 
    IIF(SCU.CourseUnits > 9, 'Fulltime', 'Parttime') AS FulltimeOrParttime, 
    SCU.CourseUnits * T.PerUnitCost + IIF(SCU.CourseUnits > 9, T.FullTimeCost, T.PartTimeCost) AS TotalTuition 
FROM 
    StudentCourseUnits SCU 
CROSS JOIN 
    dbo.Tuition T;


