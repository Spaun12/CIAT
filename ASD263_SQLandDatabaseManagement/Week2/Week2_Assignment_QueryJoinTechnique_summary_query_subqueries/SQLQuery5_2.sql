-- Get CategoryName, number of products in each category, and the highest list price in each category
SELECT c.CategoryName, COUNT(p.ProductID) AS NumberOfProducts, MAX(p.ListPrice) AS MostExpensiveProduct
FROM Categories c
JOIN Products p ON c.CategoryID = p.CategoryID
GROUP BY c.CategoryName
ORDER BY NumberOfProducts DESC;
