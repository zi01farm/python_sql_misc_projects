USE Northwind
SELECT COUNT(*) AS TotalCount FROM Orders 
WHERE Freight > 100.0 AND (ShipCountry = 'USA' OR ShipCountry = 'UK')