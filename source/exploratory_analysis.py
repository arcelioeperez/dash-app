'''
Author: Arcelio E. Perez Garcia 
Data: Keggle, insurance.csv 
Exploratory Data Analysis: 

#outputting the data for preliminary analysis 
#viewing the first 10 rows 
print(data.head(n=10))
#checking the data types 
print(data.dtypes) 

age           int64
sex          object
bmi         float64
children      int64
smoker       object
region       object
charges     float64

Based on this information, the variables 'sex', 'smoker', and 'region' need changed to numerical values instead of 'object' 
or 'string'. Region needs to be grouped e.g. 1 = southeast, 2 = soutwest, 3 = ... 

The 'charges' variable needs to be rounded in order for it to be better to come up with a prediction. 

#checking for na in the data
#print(data.isna().sum()) 
#print(data.isnull().sum())
'''
#importing libraries pandas and numpy 
import pandas as pd 


#reading the csv file 
data = pd.read_csv('insurance.csv', sep=',') 

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

#checking the data object 
#print(data.head(n=10)) 
 
''' 
Sex variable 
0 female 
1 male 

Smoker variable 
1 yes 
0 no 

Region 
3 Southwest 
2 Southeast 
1 Northwest 
0 Northeast 
''' 




