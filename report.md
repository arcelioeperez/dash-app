---
title: Report
---
# Linear Regression  
### Variables:  
Age: age of the person  
BMI: body mass index  
Sex: female (0) or male  (1)  
Children: number of children   
Smoker: smoker (1) or non-smoker (0)  
Region: southwest (3), southeast (2), northwest (1), northeast (0)  

## Code to generate the chart on the website:  
*note: this was generated in the `app.py` program*  

``` python
def update_graph(selected_dropdown):
    
    #dropdown = {'Age':'age', 'Sex':'sex', 'BMI':'bmi', 'Children':'children','Smoker':'smoker', 'Region':'region'}
    for i in selected_dropdown: 
        if i == "age": 
            dfx = df["age"]
        elif i == "sex":
            dfx = df["sex"]
        elif i == "bmi":
            dfx = df["bmi"]
        elif i == "children":
            dfx = df["children"]
        elif i == "smoker":
            dfx = df["smoker"]
        else:
            dfx = df["region"]
        dfx = np.array(dfx) 
        dfx = dfx.reshape(-1,1)
        
        #results = evaluate_model(dfx, dataY, model)
        #print("MAE (mean) and MAE (stdev): ", np.mean(results), np.std(results)) 
        model = HuberRegressor() 
        model.fit(dfx, df["charges"])
        x_range = np.linspace(dfx.min(), dfx.max(), 100) 
        y_range = model.predict(x_range.reshape(-1,1))
        figure3 = px.scatter(data,x=df[f"{i}"], y=df["charges"])
        figure3.add_traces(go.Scatter(x=x_range, y=y_range, name = "Regression Fit"))
    return figure3
```  

# Random Forest  
## What is a Random Forest?  
>
>"Random Forests grow many classification trees. \[...] Each tree gives a classification, and we say the tree 'votes' for that class. The forest chooses the classification having the most votes (over all the trees in the forest)." - [Breiman and Cutler](https://www.stat.berkeley.edu/~breiman/RandomForests/cc_home.htm)
>  

## Code used to generate the model:  
```python
def get_models(): 
    models = dict() 
    #exploting ratios from 10% to 100% 
    for i in arange(0.1, 1.1, 0.1): 
        key = "%.1f" % i 
        #setting the max samples to none 
        if i == 1.0: 
            i = None 
        models[key] = RandomForestRegressor(max_samples = i)
    return models 

def evaluate_model(model, x, y): 
    #defining the evaluation procedure 
    cv = RepeatedKFold(n_splits = 10, n_repeats = 3, random_state = 1) 
    #scores = cross_val_score(model, dataX, dataY, scoring = "neg_mean_absolute_error", cv = cv, n_jobs = 1, error_score = "raise")
    scores = cross_val_score(model, dataX, dataY, scoring = "neg_mean_squared_error", cv = cv, n_jobs = 1, error_score = "raise")

    return np.absolute(scores) 

models = get_models() 
results, names = list(), list() 

for name, model in models.items(): 
    #evaluate the model 
    scores = evaluate_model(model, dataX, dataY) 
    #storing the results 
    results.append(scores) 
    names.append(name) 
    #summarizing the performance 
    #print("Mean MAE scores and STD", name, mean(scores), std(scores)) 
    print("RMSE scores and STD", name, mean(np.sqrt(scores)))

plt.boxplot(results, labels = names, showmeans = True) 
plt.show()
```

