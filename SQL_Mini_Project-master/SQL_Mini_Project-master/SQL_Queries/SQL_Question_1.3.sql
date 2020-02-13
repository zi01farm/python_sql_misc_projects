USE Northwind

--This Query selects products which are stored in bottles
SELECT ProductName AS "Product Name", 
       CompanyName AS "Company Name", 
	   Country 
FROM Products p
JOIN Suppliers s
   ON s.SupplierID = p.SupplierID
WHERE QuantityPerUnit LIKE '%bottles';