USE my_guitar_shop2;

DELETE FROM products
WHERE productID = 6;

DELETE FROM products
WHERE categoryID = 3;

DELETE FROM categories
WHERE categoryID > 3;

DELETE FROM orderItems
WHERE orderID IN
    (SELECT orderID FROM orders
     WHERE customerID = 1);
