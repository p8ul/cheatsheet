#### Launch interactive session
psql -h localhost -U postgres;

#### Connect to a specific database
\c database_name

#### Quit the psql
\q

#### List all databases
\l

#### List all schemas
\dn

#### List all tables
\dt

#### More info on tables in current db
\dt+

#### Get detailed information on a table
\d+ table_name

### List all users
\du


### Create role
```
CREATE ROLE role_name;
```
#### Give user super admin rights
```
ALTER USER "restaurant" with superuser;
```
#### Create a new role with a username and password
CREATE ROLE username NOINHERIT LOGIN PASSWORD password;
## example 
```
create role stack with createdb superuser login password 'stack';
```

### Assign database a user
alter database property owner to property;

