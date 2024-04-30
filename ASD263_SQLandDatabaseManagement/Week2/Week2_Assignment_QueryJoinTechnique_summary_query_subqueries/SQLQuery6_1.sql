-- Select distinct CategoryName from Categories where CategoryID is in Products
SELECT DISTINCT CategoryName
FROM Categories
WHERE CategoryID IN (SELECT CategoryID FROM Products)  -- Subquery to get CategoryIDs from Products
ORDER BY CategoryName;
