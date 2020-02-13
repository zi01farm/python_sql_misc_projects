USE Northwind

--This query selects the order with the max total discount
SELECT OrderID,
       (UnitPrice * Discount) AS "Total Discount" 
FROM [Order Details]
WHERE (UnitPrice * Discount) = 
   (SELECT MAX(UnitPrice * Discount) FROM [Order Details])