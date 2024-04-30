-- Select ProductName and ListPrice where ListPrice is greater than the average ListPrice
SELECT ProductName, ListPrice
FROM Products
WHERE ListPrice > (SELECT AVG(ListPrice) FROM Products)  -- Subquery to get average ListPrice
ORDER BY ListPrice DESC;
