USE Northwind

--This query lists and orders the number of products per category
SELECT c.CategoryName AS "Category Name",
       COUNT(c.categoryID) AS "Product Count"  
FROM Categories c
JOIN Products p
   ON p.CategoryID = c.CategoryID
GROUP BY c.CategoryName, 
         c.CategoryID
ORDER BY "Product Count" DESC;