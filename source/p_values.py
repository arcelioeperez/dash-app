import statsmodels.api as sm
import pandas as pd

data = pd.read_csv("insurance.csv", delimiter = ",") 

data = pd.DataFrame(data)
predictors = data.iloc[:,:6] #all columns except 'charges'
y = data.iloc[:,-1] #charges, which is the response varible

df = data.copy()
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

df["sex"] = object_df["sex_binary"] 
df["smoker"] = object_df["smoker_binary"] 
df["region"] = object_df["region_encoded"] 

predictors = df.iloc[:,:6] #all columns except 'charges'

for i in predictors: 
	X = predictors[i]
	X = sm.add_constant(X)
	model = sm.OLS(y, X) 
	results = model.fit()
    #results.summary()
	print(f"{i} vs. charges: ", results.summary())
	print("**********************************************")
	print("**********************************************")
	print("**********************************************")
	print("P-Values:", results.pvalues)
    



