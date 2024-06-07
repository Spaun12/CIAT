USE AP;

SELECT InvoiceDate, 
    DATE_BUCKET(WEEK, 1, InvoiceDate) AS WeeklyBin, 
    DATE_BUCKET(WEEK, 1, InvoiceDate, CAST('10/8/2022' AS DATE)) 
        AS WeeklyBinWithOrigin,
    DATE_BUCKET(WEEK, 2, InvoiceDate) AS BiWeeklyBin, 
    DATE_BUCKET(YEAR, 1, InvoiceDate) AS YearlyBin 
FROM Invoices;
