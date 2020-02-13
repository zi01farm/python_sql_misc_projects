USE Northwind
SELECT OrderID, (UnitPrice * Discount) AS TotalDiscount FROM [Order Details]
WHERE (UnitPrice * Discount) = 
(SELECT MAX(UnitPrice * Discount) FROM [Order Details])