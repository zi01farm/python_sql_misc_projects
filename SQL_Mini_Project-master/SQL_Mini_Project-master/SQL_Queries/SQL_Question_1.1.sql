USE Northwind

--This query selects customers from Paris or France
SELECT CustomerID,
       CompanyName AS "Company Name",
	   Address + ', ' + City + ', ' + Country + ', ' + PostalCode AS "Address"
FROM Customers
WHERE City = 'Paris' OR City = 'London'