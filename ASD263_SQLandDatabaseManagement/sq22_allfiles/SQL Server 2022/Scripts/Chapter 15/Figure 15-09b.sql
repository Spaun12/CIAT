USE AP;

-- delete old line item data
DELETE FROM InvoiceLineItems 
WHERE InvoiceID = 114
  AND InvoiceSequence > 1;

-- declare a variable for the LineItems type
DECLARE @NewLineItems LineItems;

-- insert rows into the LineItems variable
INSERT INTO @NewLineItems VALUES (114, 2, 553, 152.25, 'Freight');
INSERT INTO @NewLineItems VALUES (114, 3, 553, 29.25, 'Freight');
INSERT INTO @NewLineItems VALUES (114, 4, 553, 48.50, 'Freight');

-- execute the stored procedure
EXEC spInsertLineItems @NewLineItems;