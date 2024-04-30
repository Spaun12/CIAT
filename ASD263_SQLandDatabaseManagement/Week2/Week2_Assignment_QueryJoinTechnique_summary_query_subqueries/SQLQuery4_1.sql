-- Select CategoryName, ProductName, and ListPrice from Categories and Products tables
SELECT c.CategoryName, p.ProductName, p.ListPrice
FROM Categories c
JOIN Products p ON c.CategoryID = p.CategoryID  -- Join on CategoryID
ORDER BY c.CategoryName, p.ProductName ASC;  -- Order by CategoryName and ProductName
