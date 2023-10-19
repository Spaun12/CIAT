DROP DATABASE IF EXISTS ap;
CREATE DATABASE ap;
USE ap;

CREATE  TABLE IF NOT EXISTS vendors (
  vendorID       INT          NOT NULL  AUTO_INCREMENT,
  vendorName     VARCHAR(45)  NOT NULL  UNIQUE,
  vendorAddress  VARCHAR(45)  NOT NULL,
  vendorCity     VARCHAR(45)  NOT NULL,
  vendorState    VARCHAR(45)  NOT NULL,
  vendorZipCode  VARCHAR(10)  NOT NULL,
  vendorPhone    VARCHAR(20)  NOT NULL,
  PRIMARY KEY (vendorID) 
);

CREATE  TABLE IF NOT EXISTS invoices (
  invoiceID      INT          NOT NULL  AUTO_INCREMENT,
  vendorID       INT          NOT NULL,
  invoiceNumber  VARCHAR(45)  NOT NULL,
  invoiceDate    DATETIME     NOT NULL,
  invoiceTotal   DECIMAL      NOT NULL,
  paymentTotal   DECIMAL,
  PRIMARY KEY (invoiceID),
  CONSTRAINT invoicesFkVendors
    FOREIGN KEY (vendorID) REFERENCES vendors (vendorID)
);

CREATE  TABLE IF NOT EXISTS lineItems (
  lineItemID     INT          NOT NULL  AUTO_INCREMENT,
  invoiceID      INT          NOT NULL,
  description    VARCHAR(45)  NOT NULL,
  quantity       INT          NOT NULL,
  price          DECIMAL      NOT NULL,
  lineItemTotal  DECIMAL      NOT NULL,
  PRIMARY KEY (lineItemID),
  CONSTRAINT lineItemsFkInvoices
    FOREIGN KEY (invoiceID) REFERENCES invoices (invoiceID)
);

CREATE INDEX vendorID
ON invoices (vendorID);

CREATE INDEX invoiceNumber
ON invoices (invoiceNumber);

CREATE INDEX invoiceID
ON lineItems (invoiceID);

CREATE USER IF NOT EXISTS ap_user
IDENTIFIED BY 'sesame';

GRANT SELECT, INSERT, UPDATE
ON *
TO ap_user;
