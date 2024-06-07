-- 6a) Let's first get a look before we so the "insert" 
-- and check the current categories
SELECT * FROM Categories;

-- 6b) Create a stored procedure to insert a new category
IF OBJECT_ID('spInsertCategory', 'P') IS NOT NULL
    DROP PROCEDURE spInsertCategory;
GO

CREATE PROCEDURE spInsertCategory
    @CategoryName NVARCHAR(255)
AS
BEGIN
    -- Insert a new category
    INSERT INTO Categories (CategoryName)
    VALUES (@CategoryName);
END;
GO

-- 6c) Test the stored procedure
-- This should succeed
EXEC spInsertCategory 'New Category';

-- This should fail (assuming 'New Category' already exists)
EXEC spInsertCategory 'New Category';

-- After insert: Verify the new categories
SELECT * FROM Categories;
