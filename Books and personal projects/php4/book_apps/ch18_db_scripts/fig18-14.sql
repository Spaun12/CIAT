USE my_guitar_shop2;

SELECT categoryID, categoryName,
	(SELECT COUNT(*) FROM products
	 WHERE products.categoryID = categories.categoryID) AS productCount
FROM categories;

SELECT c.customerID, firstName, lastName
FROM customers c
WHERE NOT EXISTS
	(SELECT * FROM orders o
	 WHERE c.customerID = o.customerID);
