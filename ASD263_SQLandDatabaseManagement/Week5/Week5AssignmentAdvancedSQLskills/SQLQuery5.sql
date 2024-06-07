-- Declare a variable and set it to the count of all products
DECLARE @ProductCount INT;
SELECT @ProductCount = COUNT(*) FROM Products;

-- Verify the product count
PRINT 'Product Count: ' + CAST(@ProductCount AS VARCHAR);

-- Check the count and display an appropriate message
IF @ProductCount >= 7
    PRINT 'The number of products is greater than or equal to 7';
ELSE
    PRINT 'The number of products is less than 7';
