SELECT t.name AS TableName, c.name AS ColumnName,
       collation_name  
FROM sys.columns c
inner join sys.tables t
  ON c.object_id = t.object_id;
