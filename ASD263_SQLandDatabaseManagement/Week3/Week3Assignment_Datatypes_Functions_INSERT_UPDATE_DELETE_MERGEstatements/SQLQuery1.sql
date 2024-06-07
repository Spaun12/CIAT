-- Check the data before the insert
SELECT * FROM Categories;

-- Insert a new category named "Brass"
INSERT INTO Categories (CategoryName)
VALUES ('Brass');

-- Check the data after the insert
SELECT * FROM Categories;
