USE AP;
GO

DROP TRIGGER IF EXISTS Invoices_UPDATE_Shipping;
GO

CREATE TRIGGER Invoices_UPDATE_Shipping
    ON Invoices
    AFTER INSERT, UPDATE
AS
    INSERT ShippingLabels
    SELECT VendorName, VendorAddress1, VendorAddress2,
           VendorCity, VendorState, VendorZipCode
    FROM Vendors v
      JOIN Inserted i
        ON v.VendorID = i.VendorID
    WHERE i.InvoiceTotal - i.PaymentTotal - i.CreditTotal = 0;

