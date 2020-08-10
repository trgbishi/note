始记于2020年7月31日<br>
[阅w3c在线sql测试](https://www.w3schools.com/sql/exercise.asp)

1.Use the NOT keyword to select all records where City is NOT "Berlin".<br>

    SELECT * FROM Customers
    WHERE NOT City = 'Berlin';

2.Select all records from the Customers where the PostalCode column is empty.<br>

    SELECT * FROM Customers WHERE PostalCode IS NULL;

3.Select all records from the Customers where the PostalCode column is NOT empty.
    
    SELECT * FROM Customers WHERE PostalCode IS NOT NULL;

4.Delete all the records from the Customers table.

    DELETE FROM Customers;

5.Select all records where the second letter of the City is an "a".
    
    SELECT * FROM Customers WHERE City LIKE '_a%';

6.Select all records where the first letter of the City is an "a" or a "c" or an "s".

    SELECT * FROM Customers WHERE City LIKE '[acs]%';

7.Select all records where the first letter of the City starts with anything from an "a" to an "f".
    
    SELECT * FROM Customers WHERE City LIKE '[a-f]%';

8.Choose the correct JOIN clause to select all records from the two tables where there is a match in both tables.

    SELECT * FROM Orders inner join Customers ON Orders.CustomerID=Customers.CustomerID;

9.Choose the correct JOIN clause to select all the records from the Customers table plus all the matches in the Orders table.

    SELECT * FROM Orders RIGHT JOIN Customers ON Orders.CustomerID=Customers.CustomerID;

10.Add a column of type DATE called Birthday.

    ALTER TABLE Persons ADD Birthday DATE;

11.Delete the column Birthday from the Persons table.
    
    ALTER TABLE Persons DROP COLUMN Birthday;