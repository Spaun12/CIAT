USE Examples;

SELECT * FROM DateSample
WHERE CONVERT(datetime, CONVERT(char(10), StartDate, 110)) = '2022-10-28';

