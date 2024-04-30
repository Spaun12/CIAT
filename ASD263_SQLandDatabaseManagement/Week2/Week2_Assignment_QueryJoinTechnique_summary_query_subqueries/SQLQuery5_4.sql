-- Get EmailAddress, number of orders, and total amount for each order for customers with more than 1 order
SELECT c.EmailAddress, COUNT(o.OrderID) AS NumberOfOrders, SUM((oi.ItemPrice - oi.DiscountAmount) * oi.Quantity) AS TotalAmount
FROM Customers c
JOIN Orders o ON c.CustomerID = o.CustomerID
JOIN OrderItems oi ON o.OrderID = oi.OrderID
GROUP BY c.EmailAddress
HAVING COUNT(o.OrderID) > 1
ORDER BY TotalAmount DESC;
