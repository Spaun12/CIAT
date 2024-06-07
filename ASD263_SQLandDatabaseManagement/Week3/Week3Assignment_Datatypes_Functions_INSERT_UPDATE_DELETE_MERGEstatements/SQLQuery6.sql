-- Select ListPrice and its variations
SELECT 
    ListPrice,
    CAST(ListPrice AS DECIMAL(10,1)) AS ListPriceDecimal,
    CONVERT(INT, ListPrice) AS ListPriceInt,
    CAST(ListPrice AS INT) AS ListPriceCastInt
FROM Products;
