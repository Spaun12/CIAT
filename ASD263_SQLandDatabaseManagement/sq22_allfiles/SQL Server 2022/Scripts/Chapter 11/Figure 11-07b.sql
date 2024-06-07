USE New_AP;

CREATE TABLE Invoices7
(InvoiceID       INT NOT NULL PRIMARY KEY,
VendorID         INT NOT NULL REFERENCES Vendors7 (VendorID),
InvoiceTotal     MONEY NULL);
