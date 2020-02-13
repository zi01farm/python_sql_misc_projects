USE Northwind
SELECT ProductName, CompanyName, Country FROM Products 
JOIN Suppliers ON Suppliers.SupplierID = Products.SupplierID
WHERE QuantityPerUnit LIKE '%bottles';