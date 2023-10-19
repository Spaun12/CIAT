USE my_guitar_shop2;

SELECT productName, listPrice, discountPercent
FROM products
WHERE listPrice < 500
ORDER BY productName;

SELECT productName, listPrice, discountPercent
FROM products
WHERE listPrice < 500
ORDER BY listPrice DESC;

SELECT productName, listPrice, discountPercent
FROM products
WHERE categoryID = 1
ORDER BY discountPercent, listPrice DESC;