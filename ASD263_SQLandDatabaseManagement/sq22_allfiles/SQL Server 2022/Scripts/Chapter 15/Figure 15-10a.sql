USE AP;

DROP PROC IF EXISTS spVendorState;
GO

CREATE PROC spVendorState
       @State varchar(20)
AS
SELECT VendorName
FROM Vendors
WHERE VendorState = @State;
