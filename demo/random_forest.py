''' 
Random Forest Analysis 
This is a regressor random forest that aims to predict the charges (insurance) based on the variables in the dataset
'''
from exploratory_analysis import data

import pandas as pd   
import matplotlib.pyplot as plt 
import numpy as np 
from numpy import mean
from numpy import std 
from numpy import arange
from sklearn.model_selection import cross_val_score 
from sklearn.model_selection import RepeatedKFold 
from sklearn.ensemble import RandomForestRegressor 

dataX = data.iloc[:,:-1] 
dataY = data.iloc[:,6]
''' 
This part of the program was adapted from a regressor model on "Machine Learning Mastery" 
url: https://machinelearningmastery.com/random-forest-ensemble-in-python/ 
*** code adapted from the above url ***
'''

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
    scores = cross_val_score(model, dataX, dataY, scoring = "neg_mean_absolute_error", cv = cv, n_jobs = 1, error_score = "raise")
    #scores = cross_val_score(model, dataX, dataY, scoring = "neg_mean_squared_error", cv = cv, n_jobs = 1, error_score = "raise")

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
    print("Mean MAE scores and STD", name, mean(scores), std(scores)) 
    #print("RMSE scores and STD", name, mean(np.sqrt(scores)))

#ans = np.sqrt(results)
#converting the ans variable to a list in order to plot it with the names list - otherwise it won't run
#ans = list(ans)
plt.boxplot(results, labels = names, showmeans = True) 
plt.show()
