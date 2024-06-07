-- Drop the view if it exists
IF OBJECT_ID('OrderItemProducts', 'V') IS NOT NULL
    DROP VIEW OrderItemProducts;
GO

-- 4a) Create the OrderItemProducts view
CREATE VIEW OrderItemProducts AS
SELECT 
    o.OrderID,
    o.OrderDate,
    o.TaxAmount,
    o.ShipDate,
    oi.ItemPrice,
    oi.DiscountAmount,
    (oi.ItemPrice - oi.DiscountAmount) AS FinalPrice,
    oi.Quantity,
    (oi.Quantity * (oi.ItemPrice - oi.DiscountAmount)) AS ItemTotal,
    p.ProductName
FROM 
    Orders o
    JOIN OrderItems oi ON o.OrderID = oi.OrderID
    JOIN Products p ON oi.ProductID = p.ProductID;
GO

-- 4b) Verify the OrderItemProducts view creation
SELECT TOP 10 *
FROM OrderItemProducts;
