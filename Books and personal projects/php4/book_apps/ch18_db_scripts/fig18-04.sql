USE my_guitar_shop2;

SELECT productName, listPrice
FROM products
WHERE categoryID = 2;

SELECT productName, listPrice
FROM products
WHERE productName = 'Gibson Les Paul';

SELECT productName, listPrice
FROM products
WHERE listPrice < 499.99;

SELECT productName, listPrice
FROM products
WHERE listPrice >= 499.99;

SELECT productName, listPrice
FROM products
WHERE productName < 'G';

SELECT productName, listPrice, dateAdded
FROM products
WHERE dateAdded < '2021-01-31';

SELECT productName, listPrice, dateAdded
FROM products
WHERE dateAdded >= '2021-01-31';

SELECT productName, listPrice, discountPercent
FROM products
WHERE discountPercent <> 30;
