-- Drop the view if it exists
IF OBJECT_ID('CustomerAddresses', 'V') IS NOT NULL
    DROP VIEW CustomerAddresses;
GO

-- 1a) Creating the CustomerAddresses view
CREATE VIEW CustomerAddresses AS
SELECT 
    c.CustomerID,
    c.EmailAddress,
    c.LastName,
    c.FirstName,
    ba.Line1 AS BillLine1,
    ba.Line2 AS BillLine2,
    ba.City AS BillCity,
    ba.State AS BillState,
    ba.ZipCode AS BillZip,
    sa.Line1 AS ShipLine1,
    sa.Line2 AS ShipLine2,
    sa.City AS ShipCity,
    sa.State AS ShipState,
    sa.ZipCode AS ShipZip
FROM 
    Customers c
    JOIN Addresses ba ON c.BillingAddressID = ba.AddressID
    JOIN Addresses sa ON c.ShippingAddressID = sa.AddressID;
GO

-- 1b) Verify the CustomerAddresses view creation works
SELECT TOP 10 *
FROM CustomerAddresses;
