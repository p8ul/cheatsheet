# Query , Update Delete data

## Query all data from a table
``` 
SELECT * FROM table_name;
```

## Query data and select only unique rows
``` 
SELECT DISTINT (column) FROM table_name;
```

## Query data from a table with filters
``` 
SELECT * FROM table WHERE condition;
```

## Assign an alias to a column in the result set
``` 
SELECT column_1 AS  new_column_1, .... FROM table_name
```

## Query data using the LIKE OPERATOR:
```
 SELECT * FROM table_name WHERE column LIKE '%value%'
```

## Query data using the BETWEEN operator;
``` 
SELECT * FROM table_name WHERE column BETWEEN low AND high;
```

## Query data using IN operator:
```
SELECT * FROM table_name WHERE column IN (value1, value2, ...);
```

## Constrain the returned rows with the LIMIT clause;
```
SELECT * FROM table_name LIMIT limit OFFSET offset ORDER BY column_name
```

## Query dat from multiple using INNER JOIN, LEFT JOIN, FULL OUTER JOIN, CROSS JION AND NATURAL JOIN

```
 SELECT * FROM table1 INNER JOIN table2 ON conditions;

 SELECT table1 LEFT JOIN table2 ON conditions;
 SELECT FROM table1 CROSS JOIN table2;
 SELECT FROM table1 NATURAL JOIN table2;
```

### Inner Join
```
SELECT column_name(s) FROM table_name1 INNER JOIN table_name2 ON
table_name1.column_name=table_name2.column_name

SELECT Employees.LastName, Employees.FirstName, Orders.OrderNo FROM
Employees INNER JOIN Orders ON Employees.P_Id=Orders.P_Id ORDER BY
Employees.LastName
```
### Outer Join
```
SELECT column_name(s) FROM table_name1 FULL OUTER JOIN table_name2 ON
table_name1.column_name=table_name2.column_name

SELECT Employees.LastName, Employees.FirstName, Orders.OrderNo FROM
Employees FULL OUTER JOIN Orders ON Employees.P_Id=Orders.P_Id ORDER
BY Employees.LastName
```
## INTERSECTS

### The INTERSECT query allows you to return the results of 2 or more
"select" queries. However, it only returns the rows selected by all
queries. If a record exists in one query and not in the other, it
will be omitted from the INTERSECT results.
```
select field1, field2, . field_n
from tables
INTERSECT
select field1, field2, . field_n
from tables;
```
```
select supplier_id, supplier_name
from suppliers
where supplier_id > 2000
INTERSECT
select company_id, company_name
from companies
where company_id > 1000
```

## UNION
The SQL UNION operator combines the result-set of two or more SELECT
statements.
```
SELECT column_name(s) FROM table_name1 UNION SELECT column_name(s)
FROM table_name2
```
## EXAMPLE
```
SELECT LastName FROM Employees
UNION
SELECT LastName FROM Customers
```
## SELECT INTO

The SELECT INTO statement selects data from one table and inserts it
into a different table.
```
SELECT * INTO new_table_name [IN externaldatabase] FROM old_tablename
SELECT * INTO Employees_Backup FROM Employees
```
## Return the number of rows of a table
```
SELECT COUNT(*) FROM table_name;
```

## Sort rows in ascending or descending order
```
SELECT column, column2, .. FROM table ORDER BY column ASC [DESC], column2 ASC [DESC], ...;
```

## Sort rows in ascending or descending order
```
SELECT column, column2, ... FROM table ORDER BY column ASC [DESC], column2 ASC [DESC];
```

## Group rows using GROUP BY clause
```
SELECT FROM table GROUP BY column_1, column_2, ...;
```

## Filter groups using the HAVING clause;
```
SELECT * FROM table GROUP BY column_1 HAVING condition;
```

# SET operations
## Combine the result set of two or more queries

```
SELECT * FROM table1 UNION SELECT * FROM table2;
```
## Minus a result using EXCEPT operator
```
SELECT * FROM table1 EXCEPT SELECT * FROM table2;
```

## Get intersection of the result sets of two queries
```
SELECT * FROM table1 INTERSECT SELECT * FROM table2;
```

# UPDATE statement
```
UPDATE <table_name>
SET <field_name> = <expression>[, ...]
[FROM <table_name> [JOIN clause]]
[WHERE <condition>];

```

# DELETE  statement

```
DELETE FROM <table_name> [WHERE <condition>];
```


cur.execute(
            """
            SELECT
               m1 as quiz, ans 
            FROM 
               (SELECT * FROM questions) m1,            
               (SELECT * FROM answers) ans            
            """
        )
