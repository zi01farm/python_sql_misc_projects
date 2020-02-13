USE Northwind

--This query selects the top 10 customers for the year 1998
SELECT TOP 10 
       CustomerID AS "Customer",
       SUM(UnitPrice * Quantity * (1 - Discount)) AS "Total Sales"
FROM Orders o
JOIN [Order Details] od
   ON o.OrderID = od.OrderID
GROUP BY CustomerID, OrderDate
HAVING YEAR(OrderDate) = 1998
ORDER BY "Total Sales" DESC;
