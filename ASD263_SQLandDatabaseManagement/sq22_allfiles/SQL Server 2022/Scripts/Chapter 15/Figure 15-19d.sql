USE AP;
/*
This script fixes the error introduced earlier
in this figure by returning the value in the
InvoiceLineItems table to its original, correct,
value for InvoiceID 98.
*/

UPDATE InvoiceLineItems
SET InvoiceLineItemAmount = 579.42
WHERE InvoiceID = 98 
  AND InvoiceSequence = 1;

/*
Also, it returns PaymentTotal and PaymentDate to 
their original values
*/
UPDATE Invoices
SET PaymentTotal = 0, 
    PaymentDate = NULL
WHERE InvoiceID = 98;
