-- Select ProductName and DiscountPercent where DiscountPercent is unique
SELECT ProductName, DiscountPercent
FROM Products
WHERE DiscountPercent IN (
  SELECT DiscountPercent
  FROM Products
  GROUP BY DiscountPercent
  HAVING COUNT(*) = 1  -- Subquery to get unique DiscountPercent values
)
ORDER BY ProductName;
