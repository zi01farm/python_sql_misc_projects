USE Northwind
SELECT CustomerID, CompanyName, Address, City, Country, PostalCode FROM Customers
WHERE City = 'Paris' OR City = 'London'