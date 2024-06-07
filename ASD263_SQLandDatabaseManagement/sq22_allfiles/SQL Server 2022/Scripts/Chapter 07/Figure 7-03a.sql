USE Examples;
 
IF OBJECT_ID('ColorSample') IS NOT NULL
   DROP TABLE ColorSample;

CREATE TABLE ColorSample (
    ID INT IDENTITY(1,1) NOT NULL,
    ColorNumber INT NOT NULL DEFAULT 0,
    ColorName VARCHAR(10) NULL
);