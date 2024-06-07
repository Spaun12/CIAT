-- Select OrderDate and its variations
SELECT 
    OrderDate,
    CONVERT(VARCHAR, OrderDate, 1) AS OrderDateSlashFormat,
    CONVERT(VARCHAR, OrderDate, 100) AS OrderDateTime12HourFormat,
    CONVERT(VARCHAR, OrderDate, 114) AS OrderTime24HourFormat
FROM Orders;
