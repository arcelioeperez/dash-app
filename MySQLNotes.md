---
title: MySQL
---
# Using MySQL to store CSV files:    

1. To open MySQL type:    
```
mysql --local-infile=1 -u root -p
```   

Type your password.    

2. Use an existing database (or create one):    
```
use database; 
```    

3. Create an empty table (with all the columns to be read and their data types):      
Example:    

```
create table data(
id int, 
latitude float, 
longitude float, 
zipcode varchar(10), 
bedrooms int, 
market varchar(25), 
location_exact char, 
room_type varchar(30), 
neighborhood varchar(100), 
price float, 
reviews float
);
```  

4. Load the data:    
```
load data local infile '/path/to/file/file.csv'
into table data
columns terminated by ','
optionally enclosed by '"'
escaped by '"'
lines terminated by '\n'
ignore 1 lines; 
```  

### Installing MySQL on Linux:    
```
sudo apt update
sudo apt install mysql-server

#configuring MySQL 
sudo mysql_secure_installation
```
