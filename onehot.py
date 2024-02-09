import pandas as pd


myframe=pd.read_csv("E:\\Sharanya\\pythonnewvsc\\Finaldataset_BMI.csv")

myframe['Extremely weak']=0
myframe['Weak']=0
myframe['Normal']=0
myframe['Overweight']=0
myframe['Obesity']=0
myframe['Extreme Obesity']=0

print(myframe)

instance=0
for i in myframe['Index']:
    if(i=="Extremely weak"):
        myframe.at[instance, 'Extremely weak'] = 1
    if(i=="Weak"):
        myframe.at[instance, 'Weak'] = 1
    if(i=="Normal"):
        myframe.at[instance, 'Normal'] = 1
    if(i=="Overweight"):
        myframe.at[instance, 'Overweight'] = 1
    if(i=="Obesity"):
        myframe.at[instance, 'Obesity'] = 1
    if(i=="Extreme Obesity"):
        myframe.at[instance, 'Extreme Obesity'] = 1
    instance=instance+1
    

print(myframe)
myframe.to_csv('E:\\Sharanya\\pythonnewvsc\\Finaldataset_BMI_output.csv', index=False)


myframe['Male']=0
myframe['Female']=0

instance=0
for i in myframe['Gender']:
    if(i=="Male"):
        myframe.at[instance, 'Male'] = 1
    if(i=="Female"):
        myframe.at[instance, 'Female'] = 1
    instance=instance+1

print(myframe)
myframe=myframe.drop(['Gender', 'Index'], axis=1)
print(myframe)
myframe=myframe.iloc[:,[8,9,0,1,2,3,4,5,6,7]]
print(myframe)
myframe.to_csv('E:\\Sharanya\\pythonnewvsc\\Finaldataset_BMI_output2.csv', index=False)

