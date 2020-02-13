USE Northwind

--This query calculates the average ship time for orders for each month
SELECT AVG(DATEDIFF(day, OrderDate, ShippedDate)) AS "Avg Ship Time",
       CONVERT(VARCHAR(10),DATEPART(Year, OrderDate)) + '-' +
	   CONVERT(VARCHAR(10),DATEPART(Month, OrderDate)) AS "Rounded Month"
FROM Orders
GROUP BY DATEPART(Year, OrderDate),
         DATEPART(Month, OrderDate)
ORDER BY DATEPART(Year, OrderDate), 
         DATEPART(Month, OrderDate)

