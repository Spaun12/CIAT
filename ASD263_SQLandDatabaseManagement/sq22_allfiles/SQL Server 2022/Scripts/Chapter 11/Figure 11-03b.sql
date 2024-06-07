USE New_AP;

CREATE TABLE Invoices
(InvoiceID        INT        PRIMARY KEY IDENTITY,
VendorID          INT        NOT NULL,
InvoiceDate       DATE       NULL,
InvoiceTotal      MONEY      NULL DEFAULT 0);
