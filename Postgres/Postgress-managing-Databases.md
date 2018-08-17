# Managing databases

## Create a new database
```CREATE DATABASE [IF NOT EXISTS] db_name;```

## Delete a database permanently
```DROP DATABASE [IF EXISTS] db_name;```

## Create a new table
```CREATE TABLE [IF NOT EXISTS] table_name(
	pk SERIAL PRIMARY KEY,
	c1 type(size) NOT NULL,
	c2 type(size) NULL,
	...
);
```
## Add a new column to table
``` ALTER TABLE table_name ADD COLUMN new_column_name TYPE;```

## Drop a column in a table
``` ALTER TABLE table_name DROP COLUMN column_name;```

## Rename a column;
``` ALTER TABLE table_name RENAME column_name TO new_column_name;```

## Add a primary key to table
```ALTER TABLE table_name ADD PRIMARY KEY (column, ....);```

## Rename a table
```ALTER TABLE table_name RENAME TO new_table_name;```

## DROP a table and its dependent objects:
``` DROP TABLE [IF EXISTS] table_name CASCADE;```



