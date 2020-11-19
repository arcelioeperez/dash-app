---
title: Data
---
# Data Cleaning Process  

## Reading the data  
```
import pandas as pd 

data = pd.read_csv("insurance.csv", delimiter = ",")
```

## Preparing the data for the models  
```
#converting data into a dataframe
data = pd.DataFrame(data = data)

#Label Encoding the data (sex, smoker, and region variables)
object_df = data.select_dtypes(include=['object']).copy()
#print(object_df.head())
#changing variables to 'category' type
object_df["sex"] = object_df["sex"].astype('category')
object_df["smoker"] = object_df["smoker"].astype('category')
object_df["region"] = object_df["region"].astype('category')

#assinging encoded variables using 'cat.codes'
object_df["sex_binary"] = object_df["sex"].cat.codes
object_df["smoker_binary"] = object_df["smoker"].cat.codes
object_df["region_encoded"] = object_df["region"].cat.codes

#assigning colums to the data object
data["sex"] = object_df["sex_binary"]
data["smoker"] = object_df["smoker_binary"]
data["region"] = object_df["region_encoded"]
```  
Data Cleaning script: [exploratory_analysis.py](https://raw.githubusercontent.com/arcelioeperez/dash-app/gh-pages/source/exploratory_analysis.py)  

## Data with categorical values  
![data](/demo/data.PNG)  
## Data with numerical values 
![data2](/demo/data2.PNG)  
## Why?  
The models used in this analysis, random forest and linear regression, use numerical variables for their analysis. If categorical values are used the models wouldn't work. In other words by converting the categorical values to numbers (following the guidelines), for example, female 0 and male 1 - the models know that the *sex* variable can be either 0 or 1.  

## Data dictionary

Age: age of the person  
BMI: body mass index  
Sex: female (0) or male  (1)  
Children: number of children   
Smoker: smoker (1) or non-smoker (0)  
Region: southwest (3), southeast (2), northwest (1), northeast (0) 
