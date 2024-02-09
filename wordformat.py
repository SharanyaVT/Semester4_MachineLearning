import pandas as pd


def labelencode_sharanya():
    myframe=pd.read_csv("E:\\Sharanya\\pythonnewvsc\\Finaldataset_BMI.csv")
    map={"Extremely weak": 0,
        "Weak": 1,
        "Normal": 2,
        "Overweight": 3,
        "Obesity": 4,
        "Extreme Obestity": 5
    }

    myframe['Index']=[map[i] for i in myframe['Index']]

    #print(myframe)

    map2={"Male":0,
        "Female":1}

    myframe['Gender']=[map2[i] for i in myframe['Gender']]

    #print(myframe)

print(labelencode_sharanya())



