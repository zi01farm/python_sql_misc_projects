USE Northwind
SELECT Categories.CategoryName, COUNT(categories.categoryID) AS ProductCount  FROM Categories 
JOIN Products ON Products.CategoryID = Categories.CategoryID
GROUP BY Categories.CategoryName, Categories.CategoryID
ORDER BY ProductCount DESC;