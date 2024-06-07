-- Selecting OrderDate and its variations
SELECT 
    OrderDate,
    YEAR(OrderDate) AS OrderYear,
    DAY(OrderDate) AS OrderDay,
    DATEADD(DAY, 30, OrderDate) AS OrderDatePlus30Days
FROM Orders;
