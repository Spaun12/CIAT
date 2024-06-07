-- Select DateAdded and its variations
SELECT 
    DateAdded,
    CAST(DateAdded AS DATE) AS DateOnly,
    CAST(DateAdded AS TIME) AS TimeOnly,
    CONCAT(MONTH(DateAdded), '/', DAY(DateAdded)) AS MonthDay
FROM Products;
