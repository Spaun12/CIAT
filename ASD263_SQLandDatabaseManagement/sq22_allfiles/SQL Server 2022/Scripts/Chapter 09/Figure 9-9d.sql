USE Examples;

SELECT * FROM DateSample
WHERE CONVERT(time, StartDate) BETWEEN '09:00:00' AND '12:59:59:999';
