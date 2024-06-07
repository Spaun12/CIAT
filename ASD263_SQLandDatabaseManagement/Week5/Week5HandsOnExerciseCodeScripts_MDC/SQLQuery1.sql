-- Declare a variable to hold the count of students who haven't graduated
DECLARE @UndergradCount INT;

-- Set the variable to the count of students who haven't graduated
SELECT @UndergradCount = COUNT(*)
FROM Students
WHERE GraduationDate IS NULL;

-- Display a message based on the count
IF @UndergradCount >= 100
BEGIN
    PRINT 'The number of undergrad students is greater than or equal to 100';
END
ELSE
BEGIN
    PRINT 'The number of undergrad students is less than 100';
END;
