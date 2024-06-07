USE Examples;

SELECT *,
	GREATEST(EnterpriseSales, DirectSales) AS GreatestSales,
	LEAST(EnterpriseSales, DirectSales) AS LeastSales
FROM EmployeeSales;