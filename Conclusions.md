# Conclusions  

## Linear Regression:  

Pitfalls of using different packages:  
1. Read the documentation of the package or library.  
2. Understand what the given function is trying to accomplish.  

Example:  

Using `sklearn` in Python and `lm()` in R had the same R Squared, coefficients, and other metrics. However, the `statsmodels.api` package had different results for every variable. The reason was that the `statsmodels.api` package doesn't immediately include the **intercept** - the user must create a **constant** based on the `X` (predictor) in order to get the same results.  

This was my **mistake**:  
```python
X = data["age"]
model = sm.OLS(y, X)

results = model.fit()
print(result.summary())
```  

Here is the **correction** to that mistake:  
```python
X = data["age"]
X = sm.add_constant(X)
model = sm.OLS(y, X) 

result = model.fit()
print(result.summary())
```  
**Note:** The only line that changed was `X = sm.add_constant(X)`.  

If doing multiple regressions for every single variable, consider doing:  
```python
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
```  



