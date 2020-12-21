---
title: MySQLNotes
---
# Using MySQL to store CSV files  

**Installing MySQL on Linux:**      
```
sudo apt update
sudo apt install mysql-server

#configuring MySQL 
sudo mysql_secure_installation
```  

**To open MySQL type:**     
```
mysql --local-infile=1 -u root -p
```    

**Use an existing database (or create one):**     
```
use database; 
```    
**Create an empty table (with all the columns to be read and their data types):**      

*Example:*    
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

**Load the data:**    
```
load data local infile '/path/to/file/file.csv'
into table data
columns terminated by ','
optionally enclosed by '"'
escaped by '"'
lines terminated by '\n'
ignore 1 lines; 
```  

#### MySQL Documentation 
[MySQL](https://dev.mysql.com/doc/)  

# Alternatively, you can use `tomysqlv2`  

This program was developed using SQLAlchemy, Pandas, MySQLClient and PyMySQL. It lets you input a CSV file, your MySQL credentials, and the name for the table.  

It then processes the information, creates the MySQL table (with the correct data types), and transfers the CSV file to MySQL. 

**More Infomation [here](https://github.com/arcelioeperez/csvtomysql)**    

**Download here [tomysqlv2](https://raw.githubusercontent.com/arcelioeperez/csvtomysql/main/tomysqlv2)**
