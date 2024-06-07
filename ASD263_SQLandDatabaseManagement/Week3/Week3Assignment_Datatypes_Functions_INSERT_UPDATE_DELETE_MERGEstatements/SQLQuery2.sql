-- Check the data before the update
SELECT * FROM Categories WHERE CategoryName = 'Brass';

-- Update the category name from "Brass" to "Woodwinds"
UPDATE Categories
SET CategoryName = 'Woodwinds'
WHERE CategoryName = 'Brass';

-- Check the data after the update
SELECT * FROM Categories WHERE CategoryName = 'Woodwinds';
