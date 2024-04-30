-- Count the number of orders and sum the TaxAmount
SELECT COUNT(*) AS NumberOfOrders, SUM(TaxAmount) AS TotalTaxAmount
FROM Orders;
