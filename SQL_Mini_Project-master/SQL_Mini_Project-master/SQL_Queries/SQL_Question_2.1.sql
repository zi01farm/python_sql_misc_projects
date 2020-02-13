USE Mini_Project

--This Statement Creates a 'Spartans' Table in a Mini_project DB
DROP TABLE Spartans;
CREATE TABLE Spartans(
   SpartanID INT NOT NULL IDENTITY PRIMARY KEY,
   Title VARCHAR(5),
   First_name VARCHAR(25),
   Last_name VARCHAR(40),
   University VARCHAR(40),
   Course VARCHAR(40),
   Mark VARCHAR(5)
   );