/*
NOTE: Make sure to set the role_principle_id column 
      to the ID from the query in 17-14a
*/
SELECT member_principal_id, name
FROM sys.server_role_members srm
  JOIN sys.server_principals sp
    ON srm.member_principal_id = sp.principal_id
WHERE srm.role_principal_id = 271;