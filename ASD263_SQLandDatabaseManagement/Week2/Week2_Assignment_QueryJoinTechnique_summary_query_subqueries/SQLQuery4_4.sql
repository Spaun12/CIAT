SELECT c.LastName, c.FirstName, o.OrderDate, p.ProductName, oi.ItemPrice, oi.DiscountAmount, oi.Quantity
FROM Customers c
JOIN Orders o ON c.CustomerID = o.CustomerID
JOIN OrderItems oi ON o.OrderID = oi.OrderID
JOIN Products p ON oi.ProductID = p.ProductID
ORDER BY c.LastName, o.OrderDate, p.ProductName;
