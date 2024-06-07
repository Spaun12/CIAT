-- Select CardNumber and its variations
SELECT 
    CardNumber,
    LEN(CardNumber) AS CardNumberLength,
    RIGHT(CardNumber, 4) AS LastFourDigits,
    CONCAT('XXXX-XXXX-XXXX-', RIGHT(CardNumber, 4)) AS MaskedCardNumber
FROM Orders;
