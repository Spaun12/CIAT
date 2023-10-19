USE my_guitar_shop2;

SELECT productName FROM products
WHERE productName LIKE 'Fender%';

SELECT productName FROM products
WHERE productName LIKE '%cast%';

SELECT zipCode FROM addresses
WHERE zipCode LIKE '076__';

SELECT orderDate FROM orders
WHERE orderDate LIKE '2022-01-__%';
