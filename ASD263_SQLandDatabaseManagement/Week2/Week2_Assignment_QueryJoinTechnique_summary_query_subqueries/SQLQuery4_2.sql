-- Select customer details for a specific email address
SELECT c.FirstName, c.LastName, a.Line1, a.City, a.State, a.ZipCode
FROM Customers c
JOIN Addresses a ON c.CustomerID = a.CustomerID  -- Join on CustomerID
WHERE c.EmailAddress = 'allan.sherwood@yahoo.com';  -- Filter for a specific email address
