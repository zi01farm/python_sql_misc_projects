USE Northwind

--This query selects Employees and who they report to, those who report to no one 
--have a NULL value next to their name
SELECT e1.TitleOfCourtesy + ' ' + e1.FirstName + ' ' + e1.LastName AS "Employee Name",
       e2.TitleOfCourtesy + ' ' + e2.FirstName + ' ' + e2.LastName AS "Reporting to..."
FROM Employees e1
LEFT JOIN Employees e2
   ON e1.ReportsTo = e2.EmployeeID