# dbselect
A python package for generating SQL select statements. As the package name suggest, this package focuses only at generating the SQL select statements. 

## Usage:

```python
from dbselect import dbselect
sql = dbselect.generate('employee')
print(sql)
```
results in 

```sql
select * from employee
```

However if we want to select some specific columns only (say name and hire_date) then we need to pass a configuration object (a dict) containing a `'columns'` key with `'name,hire_date'` as value 

```python
sql = dbselect.generate('employee', {'columns': 'name,hire_date'})
```
results in 

```sql
select name,hire_date from employee
```

The configuration object (a dict) supports the following keys:

Key | Description | Example
----|-------------|---------
columns | Specify list of columns to be selected | `'columns':'name,hire_date'` or <br> `'columns':['name','hire_date']`
order_by | Specify list of columns to be used for ordering | `'order_by':'name'` or <br> `'order_by':['name']`
asc_desc | Specify ascending or descending order of given order by columns | `'asc_desc':'desc'` or <br> `'asc_desc':['desc']`
limit | Specify the maximum rows the select statement should return (defaults to 1000) | `'limit':'10000'`

The above 'keys' are considered standard keys of the configuration object. Any other keys defined in the configuraiton object are considered row filters i.e. they are added to the where clause.

