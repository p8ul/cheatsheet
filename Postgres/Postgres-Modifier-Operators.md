# Operators
```
> Greater than
```
```
< Less than 
```
```
>=    <=    = BETWEEN LIKE IN

```

# Modifiers
## AND OR
```
SELECT * FROM Employees WHERE City=‘Plano' AND LastName=‘Johnson‘
SELECT * FROM Employees WHERE City=‘Plano' OR City=‘Frisco'
```
## Order By
SELECT column_name(s) FROM table_name ORDER BY column_name(s) ASC|DESC

## Between
### The BETWEEN operator selects a range of data between two values.
```
SELECT column_name(s)
FROM table_name
WHERE column_name
BETWEEN value1 AND value2
```

```
SELECT * FROM Employees
WHERE LastName
BETWEEN 'Jones' AND 'McMurray'
```

