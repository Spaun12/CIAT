-- Drop the function if it exists
IF OBJECT_ID('fnDiscountPrice', 'FN') IS NOT NULL
    DROP FUNCTION fnDiscountPrice;
GO

-- 7a) Create a function to calculate the discount price
CREATE FUNCTION fnDiscountPrice (@ItemID INT)
RETURNS DECIMAL(10, 2)
AS
BEGIN
    DECLARE @DiscountPrice DECIMAL(10, 2);
    
    SELECT @DiscountPrice = (ItemPrice - DiscountAmount)
    FROM OrderItems
    WHERE ItemID = @ItemID;
    
    RETURN @DiscountPrice;
END;
GO

-- 7b) Verify the function creation by using it in a SELECT statement
SELECT 
    ItemID,
    ItemPrice,
    DiscountAmount,
    dbo.fnDiscountPrice(ItemID) AS DiscountPrice
FROM 
    OrderItems;
