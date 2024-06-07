USE AP;

-- drop stored procedure if it exists already
DROP PROC IF EXISTS spInsertLineItems;
GO

-- drop table type if it exists already
DROP TYPE IF EXISTS LineItems;
GO

-- create the user-defined table type named LineItems
CREATE TYPE LineItems AS
TABLE
(InvoiceID        int           NOT NULL,
 InvoiceSequence  smallint      NOT NULL,
 AccountNo        int           NOT NULL,
 ItemAmount       money         NOT NULL,
 ItemDescription  varchar(100)  NOT NULL,
PRIMARY KEY (InvoiceID, InvoiceSequence));

GO

-- create a stored procedure that accepts the LineItems type
CREATE PROC spInsertLineItems
    @NewLineItems LineItems READONLY
AS
    INSERT INTO InvoiceLineItems
    SELECT *
    FROM @NewLineItems;

GO