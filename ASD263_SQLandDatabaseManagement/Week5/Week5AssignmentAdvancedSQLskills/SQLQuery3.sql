-- 3a) First lets check the current shipping address for the customer with ID 8
SELECT ShippingAddressID, Line1
FROM Customers c
JOIN Addresses a ON c.ShippingAddressID = a.AddressID
WHERE c.CustomerID = 8;

-- 3b) Update the shipping address for a specific customer in the CustomerAddresses view
UPDATE Addresses
SET Line1 = '1990 Westwood Blvd.'
WHERE AddressID = (
    SELECT ShippingAddressID 
    FROM Customers 
    WHERE CustomerID = 8
);

-- 3c) After update: Verify the shipping address for the customer 
SELECT ShippingAddressID, Line1
FROM Customers c
JOIN Addresses a ON c.ShippingAddressID = a.AddressID
WHERE c.CustomerID = 8;
