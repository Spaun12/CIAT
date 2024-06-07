USE Examples;

SELECT * FROM DateSample
WHERE DATETRUNC(DAY, StartDate) = '2022-10-28';
