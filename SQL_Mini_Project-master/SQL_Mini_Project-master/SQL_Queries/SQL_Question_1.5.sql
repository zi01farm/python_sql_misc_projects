USE Northwind

--This query prints the full name of each employee and what city they are in
SELECT CONCAT(TitleOfCourtesy,' ', FirstName, ' ', LastName) AS FullName,
       City 
FROM Employees
