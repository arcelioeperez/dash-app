from exploratory_analysis import data  
''' 

*note: to run these files you need to have them in your cwd (current work directory). 
I will zip all the files in order for it to run. 

If running on the terminal, you must type: 
$python statistical_significance.py 
-- where '$' is the terminal promp 

If running on an IDE (i.e. Spyder, Eclipse, PyCharm): 
just press the run button 

If running on VIM or Emacs: 
run from the terminal promp with the instructions explained above

Remember that this program is only executed if the 'code' is inside the 
if __name__ == "__main__" declaration. 
Also, the first import statement is the 1st module, 'exploratory_analysis.py' 
However, when importing it you must type: 
from exploratory_analysis import data 

The reason is that we just want to import the data, in this case the csv file 
that was cleaned and grouped in order to work for linear regression models. 
 
'''

if __name__  == "__main__": 
    import pandas as pd 
    import numpy as np 
    import matplotlib.pyplot as plt
    ''' 
    Plotting Histograms
    '''
    #plotting histograms/bar charts
    fig, ax = plt.subplots(nrows = 2, ncols = 3) 
    ax[0,0].hist(data["age"])
    ax[0,0].set_title("Age",fontsize = 10)
    ax[0,1].hist(data["sex"])
    ax[0,1].set_title("Sex", fontsize = 10)
    ax[1,0].hist(data["bmi"])
    ax[1,0].set_title("BMI", fontsize =10)
    ax[1,1].hist(data["children"])
    ax[1,1].set_title("Number of Children", fontsize = 10)
    ax[0,2].hist(data["smoker"])
    ax[0,2].set_title("Smoker", fontsize = 10)
    ax[1,2].hist(data["region"])
    ax[1,2].set_title("Region", fontsize = 10)
    for ax in fig.get_axes(): 
        ax.label_outer()

    plt.show()

    #count number of occurences in the data 
    ''' 
    As previously mentioned, 

    sex: 
    female 0 
    male 1

    smoker:
    yes 1 
    no 0

    region:
    southwest 3
    southeast 2
    northwest 1
    northeast 0
    '''
    count_age = data["age"].value_counts()
    count_sex = data["sex"].value_counts() 
    count_children = data["children"].value_counts() 
    count_smoker = data["smoker"].value_counts() 
    count_region = data["region"].value_counts()

    #printing out the counts and exporting to a text file 
    #this step was made using the terminal command: 
    #$python statistical_significance.py > stats.txt 

    print("The number of females is: ", count_sex[0]) 
    print("The number of males is: ", count_sex[1]) 

    print("The number of smokers is: ", count_smoker[1]) 
    print("The number of non-smokers is: ", count_smoker[0]) 

    print("The number of people in the Southwest is: ", count_region[3]) 
    print("The number of people in the Southeast is: ", count_region[2]) 
    print("The number of people in the Northwest is: ", count_region[1]) 
    print("The number of people in the Northeast is: ", count_region[0]) 
    
    '''
    In order to be more descriptive I decided to include the original values from the original CSV file
    i.e. with 'female' instead of '0', etc. 

    '''
    df = pd.read_csv("insurance.csv", sep = ",")
    print("The highest value charged was: ", df["charges"].max()) 
    print("The lowest value charged was:", df["charges"].min())
    #returns the row of the highest charge amount
    row_highest = df.iloc[df["charges"].idxmax()] 
    #returns the row of the lowest charge amount
    row_lowest = df.iloc[df["charges"].idxmin()] 

    print("The row with the highest charged amount: ", row_highest) 
    print("The row with the lowest charged amount: ", row_lowest)
