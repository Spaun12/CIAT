-- Get EmailAddress, total price of ordered items, and total discount for each customer
SELECT c.EmailAddress, SUM(oi.ItemPrice * oi.Quantity) AS TotalPrice, SUM(oi.DiscountAmount * oi.Quantity) AS TotalDiscount
FROM Customers c
JOIN Orders o ON c.CustomerID = o.CustomerID
JOIN OrderItems oi ON o.OrderID = oi.OrderID
GROUP BY c.EmailAddress
ORDER BY TotalPrice DESC;
