USE Northwind

--This query counts how many freight orders from the UK or USA had an amount larger than 100"
SELECT COUNT(*) AS "Total Count" 
FROM Orders 
WHERE Freight > 100.0 AND (ShipCountry = 'USA' OR ShipCountry = 'UK')