USE my_guitar_shop2;

SELECT productName, listPrice, discountPercent, categoryID
FROM products
WHERE categoryID = 1 AND discountPercent = 30;

SELECT productName, listPrice, discountPercent, categoryID
FROM products
WHERE categoryID = 1 OR discountPercent = 30;

SELECT productName, listPrice
FROM products
WHERE NOT listPrice >= 500;

SELECT productName, listPrice
FROM products
WHERE listPrice < 500;

SELECT productName, listPrice, discountPercent, dateAdded
FROM products
WHERE dateAdded > '2021-07-01' OR listPrice < 500
AND discountPercent > 25;

SELECT productName, listPrice, discountPercent, dateAdded
FROM products
WHERE (dateAdded > '2021-07-01' OR listPrice < 500)
AND discountPercent > 25;