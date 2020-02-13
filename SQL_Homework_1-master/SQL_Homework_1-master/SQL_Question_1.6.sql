USE Northwind
SELECT RegionDescription, ROUND(SUM(UnitPrice * Quantity), 0) AS TotalSales FROM Territories
JOIN Region ON Territories.RegionID = Region.RegionID
JOIN EmployeeTerritories ON Territories.TerritoryID = EmployeeTerritories.TerritoryID
JOIN Orders ON EmployeeTerritories.EmployeeID = Orders.EmployeeID
JOIN [Order Details] ON [Order Details].OrderID = Orders.OrderID
GROUP BY RegionDescription HAVING SUM(UnitPrice * Quantity) > 1000000;