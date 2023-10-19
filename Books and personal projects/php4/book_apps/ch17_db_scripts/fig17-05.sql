DROP DATABASE IF EXISTS my_ch17_shop05;

CREATE DATABASE my_ch17_shop05;

USE my_ch17_shop05;

CREATE TABLE customers (
  customerID    INT           NOT NULL   PRIMARY KEY  AUTO_INCREMENT,
  emailAddress  VARCHAR(255)  NOT NULL   UNIQUE,
  firstName     VARCHAR(30)   NOT NULL
);

INSERT INTO customers 
VALUES(1, 'joelmurach@yahoo.com', 'Joelhasalongfirstname');

-- A table with a column-level foreign key constraint
CREATE TABLE orders1
(
	orderID INT PRIMARY KEY,
	customerID INT NOT NULL REFERENCES customers (customerID),
	orderDate DATETIME NOT NULL
);

-- A table with a table-level foreign key constraint
CREATE TABLE orders2
(
	orderID INT PRIMARY KEY,
	customerID INT NOT NULL,
	orderDate DATETIME NOT NULL,
	CONSTRAINT ordersFkCustomers
		FOREIGN KEY (customerID) REFERENCES customers (customerID)
);

-- A table with a table-level foreign key constraint 
-- that uses the ON DELETE clause
CREATE TABLE orders3
(
	orderID INT PRIMARY KEY,
	customerID INT NOT NULL,
	orderDate DATETIME NOT NULL,
	CONSTRAINT orders2FkCustomers
		FOREIGN KEY (customerID) REFERENCES customers (customerID)
		ON DELETE CASCADE
);

-- An INSERT statement that fails because a related row doesn’t exist
INSERT INTO orders2
VALUES (1, 999, '2022-04-03');

