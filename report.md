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
