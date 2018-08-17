# Modifying data
## Insert a new row into a table
``` INSERT INTO table_name(column1,column2,..)
VALUES(value1,value2,...),
    (value1,value1,...)..```

## Update data for all rows:
``` UPDATE table_name SET column1 = value1,.. WHERE condition; ```

## DELETE ALL ROWS of a table:
``` DELETE FROM table_name;```

## Delete specific rows based on conditions
``` DELETE FROM table_name WHERE condition;```

# Performance
## Show the query plan for a query
``` EXPLAIN query;```
## Show and execute the query plan for query
``` EXPLAIN ANALYZE query;```

## Collect statistics
``` ANALYZE table_name;```

