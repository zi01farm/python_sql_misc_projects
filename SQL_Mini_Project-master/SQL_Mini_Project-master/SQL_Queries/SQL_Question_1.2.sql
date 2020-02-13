USE Northwind

--This query selects products which come in bottles
SELECT * 
FROM Products 
WHERE QuantityPerUnit LIKE '%bottles'