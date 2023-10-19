DROP DATABASE IF EXISTS my_ch17_shop03;

CREATE DATABASE my_ch17_shop03;

USE my_ch17_shop03;

-- A statement that creates a table without column attributes
CREATE TABLE customers1
(
  customerID  INT,
  firstName   VARCHAR(60),
  lastName    VARCHAR(60)
);

-- A statement that creates a table with column attributes
CREATE TABLE customers2
(
  customerID  INT           NOT NULL   UNIQUE,
  firstName   VARCHAR(60)   NOT NULL,
  lastName    VARCHAR(60)   NOT NULL
);

-- Another statement that creates a table with column attributes
CREATE TABLE orders
(
  orderID      INT           NOT NULL   UNIQUE,
  vendorID     INT           NOT NULL,
  orderNumber  VARCHAR(50)   NOT NULL,
  orderDate    DATE          NOT NULL,
  orderTotal   DECIMAL(9,2)  NOT NULL,
  paymentTotal DECIMAL(9,2)             DEFAULT 0
);