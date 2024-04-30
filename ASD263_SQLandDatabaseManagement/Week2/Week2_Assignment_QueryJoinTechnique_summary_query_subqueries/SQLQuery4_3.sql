-- Select customer details for shipping addresses
SELECT c.FirstName, c.LastName, a.Line1, a.City, a.State, a.ZipCode
FROM Customers c
JOIN Addresses a ON c.ShippingAddressID = a.AddressID  -- Join on ShippingAddressID
