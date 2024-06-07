-- First check the data before the insert
SELECT * FROM Products;

-- Insert a new product with specified values
INSERT INTO Products (CategoryID, ProductCode, ProductName, Description, ListPrice, DiscountPercent, DateAdded)
VALUES (4, 'dgx_640', 'Yamaha DGX 640 88-Key Digital Piano', 'Long description to come.', 799.99, 0, GETDATE());

-- Check and confirm the data after the insert
SELECT * FROM Products;