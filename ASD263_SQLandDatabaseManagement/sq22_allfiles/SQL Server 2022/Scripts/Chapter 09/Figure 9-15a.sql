SELECT
	LEAST(1,2,3) AS LeastNumber,
	GREATEST(1,2,3) AS GreatestNumber,
	LEAST('Apple','Bannana','Pear') AS LeastString,
	GREATEST('Apple','Bannana','Pear') AS GreatestString,
	LEAST(CONVERT(DATE, '2023-01-01'),CONVERT(DATE, '2023-01-31')) AS LeastDate,
	GREATEST(CONVERT(DATE, '2023-01-01'),CONVERT(DATE, '2023-01-31')) AS GreatestDate;