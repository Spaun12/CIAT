DROP DATABASE IF EXISTS my_ch17_shop12;

CREATE DATABASE my_ch17_shop12;

USE my_ch17_shop12;

CREATE TABLE customers (
  customerID    INT           NOT NULL   PRIMARY KEY  AUTO_INCREMENT,
  emailAddress  VARCHAR(255)  NOT NULL   UNIQUE,
  firstName     VARCHAR(30)   NOT NULL
);

CREATE TABLE products (
  productID     INT           NOT NULL   PRIMARY KEY  AUTO_INCREMENT,
  name          VARCHAR(30)   NOT NULL,
  description   VARCHAR(255)  NOT NULL,
  listPrice     DECIMAL(9,2)  NOT NULL   DEFAULT 0
);

GRANT SELECT, INSERT, UPDATE, DELETE
ON my_ch17_shop12.customers
TO joel IDENTIFIED BY 'sesame';

GRANT ALL 
ON *.*
TO dba IDENTIFIED BY 'supersecret'
WITH GRANT OPTION;

REVOKE ALL, GRANT OPTION 
FROM dba;

REVOKE UPDATE, DELETE
ON my_ch17_shop12.customers FROM joel;

DROP USER joel;
DROP USER dba;