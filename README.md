# dbselect
Generate SQL select statement

## Usage:

```
from dbselect import dbselect
sql = dbselect.generate_select('employee')
print(sql)
```
results in 

```
select * from employee
```

However if we want to select some specific columns only (say name and hire_date) then we need to pass a dictionary object containing a 'columns' key with 'name,hire_date' as value 

```
sql = dbselect.generate_select('employee', {'columns': 'name,hire_date'})
```
results in 

```
select name,hire_date from employee
```

Dictionary object supports the following keys:

Key | Description | Example
----|-------------|---------
columns | Specify list of columns to be selected | 'columns':'name,hire_date' or 'columns':['name','hire_date']
order_by | Specify list of columns to be used for ordering | 'order_by':'name' or 'order_by':['name']


