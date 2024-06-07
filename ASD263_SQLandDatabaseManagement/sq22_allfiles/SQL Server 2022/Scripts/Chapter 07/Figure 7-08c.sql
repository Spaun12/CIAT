USE AP;

DELETE Invoices
WHERE InvoiceTotal - PaymentTotal - CreditTotal = 0;
