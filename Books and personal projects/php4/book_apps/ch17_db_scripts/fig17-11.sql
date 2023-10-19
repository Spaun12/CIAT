DROP DATABASE IF EXISTS my_ch17_shop11;

CREATE DATABASE my_ch17_shop11;

USE my_ch17_shop11;

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

-- Example 1: Create a user with no privileges
GRANT USAGE
ON *.* 
TO joel IDENTIFIED BY 'sesame';

-- Example 2: Create a user with database privileges
GRANT SELECT, INSERT, UPDATE, DELETE
ON my_ch17_shop11.*
TO ch17user IDENTIFIED BY 'pa55word';

-- Example 3: Create a user with global privileges
GRANT ALL 
ON *.*
TO dba IDENTIFIED BY 'supersecret'
WITH GRANT OPTION;

-- Example 4: Grants table privileges to a user
GRANT SELECT, INSERT, UPDATE
ON my_ch17_shop11.products TO joel;

-- Example 5: Grant database privileges to a user
GRANT SELECT, INSERT, UPDATE
ON my_ch17_shop11.* TO joel;

-- Example 6: Grant global privileges to a user
GRANT SELECT, INSERT, UPDATE
ON *.* TO joel;

-- Example 7: Grants column privileges to a user
GRANT SELECT (name, description, listPrice), UPDATE (description)
ON my_ch17_shop11.products TO joel;

-- Example 8: Use the default database
GRANT SELECT, INSERT, UPDATE, DELETE
ON customers TO joel;

-- Example 9: Create multiple users
GRANT SELECT, INSERT, UPDATE, DELETE
ON my_ch17_shop11.*
TO mike IDENTIFIED BY 'pa55word',
   anne IDENTIFIED BY 'pa55word',
   ben IDENTIFIED BY 'pa55word'
WITH GRANT OPTION;

-- Test
GRANT CREATE
ON my_ch17_shop11.*
TO joel;

DROP USER joel, ch17user, dba, mike, anne, ben;

