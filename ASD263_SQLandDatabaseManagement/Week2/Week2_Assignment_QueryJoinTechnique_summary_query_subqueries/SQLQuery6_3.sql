-- Select CategoryName where there does not exist a product with the same CategoryID
SELECT CategoryName
FROM Categories c
WHERE NOT EXISTS (SELECT * FROM Products p WHERE c.CategoryID = p.CategoryID);  -- Subquery to check if a product exists with the same CategoryID
