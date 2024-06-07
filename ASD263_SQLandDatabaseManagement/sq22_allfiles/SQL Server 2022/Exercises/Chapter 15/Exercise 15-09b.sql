USE AP;
GO

CREATE TRIGGER NoDuplicates
ON TestUniqueNulls
AFTER INSERT, UPDATE AS
BEGIN
   IF
    (SELECT COUNT(*)
     FROM TestUniqueNulls t
       JOIN Inserted i
         ON t.NoDupName = i.NoDupName) > 1
   BEGIN
    ROLLBACK TRAN;
	THROW 50001, 'Duplicate value.', 1;
   END;
END;
