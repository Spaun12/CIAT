USE AP;

DROP FUNCTION IF EXISTS fnVendorID;
GO

CREATE FUNCTION fnVendorID
    (@VendorName varchar(50))
    RETURNS int
BEGIN
    RETURN (SELECT VendorID FROM Vendors WHERE VendorName = @VendorName);
END;
