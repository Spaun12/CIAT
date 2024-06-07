-- Checking the data before the delete
SELECT * FROM Categories WHERE CategoryName = 'Woodwinds';

-- Delete the "Woodwinds" category
DELETE FROM Categories
WHERE CategoryName = 'Woodwinds';

-- Checking the data after the delete
SELECT * FROM Categories;
