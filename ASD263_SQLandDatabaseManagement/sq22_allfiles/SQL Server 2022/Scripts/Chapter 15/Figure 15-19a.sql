USE AP;
/*
This script introduces an error 
by updating the InvoiceLineItems table 
to have an incorrect value for one of the line 
items for InvoiceID 100.
*/

UPDATE InvoiceLineItems
SET InvoiceLineItemAmount = 477.79
WHERE InvoiceID = 98
  AND InvoiceSequence = 1;
