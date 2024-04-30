-- Modify the previous query to only count and total line items with an ItemPrice greater than 400
SELECT c.EmailAddress, COUNT(o.OrderID) AS NumberOfOrders, SUM((oi.ItemPrice - oi.DiscountAmount) * oi.Quantity) AS TotalAmount
FROM Customers c
JOIN Orders o ON c.CustomerID = o.CustomerID
JOIN OrderItems oi ON o.OrderID = oi.OrderID
WHERE oi.ItemPrice > 400
GROUP BY c.EmailAddress
HAVING COUNT(o.OrderID) > 1
ORDER BY TotalAmount DESC;
