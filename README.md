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

However if we want to select some specific columns only (say name and hire_date) then we need to pass a dictionary object containing a `'columns'` key with `'name,hire_date'` as value 

```python
sql = dbselect.generate('employee', {'columns': 'name,hire_date'})
```
results in 

```sql
select name,hire_date from employee
```

Dictionary object supports the following keys:

Key | Description | Example
----|-------------|---------
columns | Specify list of columns to be selected | `'columns':'name,hire_date'` or <br> `'columns':['name','hire_date']`
order_by | Specify list of columns to be used for ordering | `'order_by':'name'` or <br> `'order_by':['name']`


