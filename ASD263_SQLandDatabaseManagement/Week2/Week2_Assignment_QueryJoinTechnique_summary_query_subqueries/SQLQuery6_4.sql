-- Select EmailAddress, OrderID, and order total for each order
WITH OrderTotals AS (
  SELECT c.EmailAddress, o.OrderID, SUM(oi.ItemPrice * oi.Quantity) AS OrderTotal  -- Subquery to get order totals for each order
  FROM Customers c
  JOIN Orders o ON c.CustomerID = o.CustomerID
  JOIN OrderItems oi ON o.OrderID = oi.OrderID
  GROUP BY c.EmailAddress, o.OrderID
)
SELECT EmailAddress, MAX(OrderTotal) AS LargestOrder  -- Select EmailAddress and the largest order total
FROM OrderTotals
GROUP BY EmailAddress;
