-- Checking the data before the update
SELECT * FROM Products WHERE ProductCode = 'dgx_640';

-- Update the DiscountPercent for the product added
UPDATE Products
SET DiscountPercent = 35
WHERE ProductCode = 'dgx_640';

-- Checking after the update
SELECT * FROM Products WHERE ProductCode = 'dgx_640';
