DROP DATABASE IF EXISTS my_ch17_shop07;

CREATE DATABASE my_ch17_shop07;

USE my_ch17_shop07;

DROP TABLE IF EXISTS customers;

CREATE TABLE customers (
  customerID    INT           NOT NULL   PRIMARY KEY  AUTO_INCREMENT,
  emailAddress  VARCHAR(255)  NOT NULL   UNIQUE,
  firstName     VARCHAR(30)   NOT NULL
);

