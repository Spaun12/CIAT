USE my_guitar_shop2;

SELECT categoryID, COUNT(*) AS productCount, 
       AVG(listPrice) AS averageListPrice
FROM products
GROUP BY categoryID
ORDER BY productCount;

SELECT categoryName, COUNT(*) AS productCount,
       AVG(listPrice) AS averageListPrice
FROM products p JOIN categories c
   ON p.categoryID = c.categoryID 
GROUP BY categoryName
HAVING averageListPrice > 400;

SELECT categoryName, COUNT(*) AS productCount,
       AVG(listPrice) AS averageListPrice
FROM products p JOIN categories c
   ON p.categoryID = c.categoryID 
WHERE listPrice > 400
GROUP BY categoryName;
