USE Northwind

--this query selects regions where total sales were over 1 million
SELECT RegionDescription AS "Region Description",
       ROUND(SUM(UnitPrice * Quantity), 0) AS "Total Sales" 
FROM Territories t
JOIN Region r 
   ON t.RegionID = r.RegionID
JOIN EmployeeTerritories empt 
   ON t.TerritoryID = empt.TerritoryID
JOIN Orders o 
   ON empt.EmployeeID = o.EmployeeID
JOIN [Order Details] od
   ON od.OrderID = o.OrderID
GROUP BY RegionDescription 
HAVING SUM(UnitPrice * Quantity) > 1000000;