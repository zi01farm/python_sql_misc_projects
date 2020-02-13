USE Northwind

--This query lists and orders all supplier with total sales over 10,000
SELECT s.CompanyName AS "Company Name",
       ROUND(SUM(od.UnitPrice * od.Quantity * (1 - od.Discount)),0) AS "Total Sales"
FROM [Order Details] od
JOIN Products p
   ON od.ProductID = p.ProductID
JOIN Suppliers s
   ON p.SupplierID = s.SupplierID
GROUP BY s.CompanyName
HAVING SUM(od.UnitPrice * od.Quantity * (1 - od.Discount)) > 10000
ORDER BY SUM(od.UnitPrice * od.Quantity * (1 - od.Discount));


