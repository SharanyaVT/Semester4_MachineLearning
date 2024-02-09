import pandas as pd
import math

def euciladean(vector1,vector2,n):
        sum=0
        for i in range(0,n):
            sum=sum+(vector2[i]-vector1[i])**2
        #print(sum)
        return(math.sqrt(sum))

def knnclassifer_sharanya():
    myframe=pd.read_csv("E:\\Sharanya\\pythonnewvsc\\Finaldataset_BMI.csv")
    map={"Extremely weak": 0,
        "Weak": 1,
        "Normal": 2,
        "Overweight": 3,
        "Obesity": 4,
        "Extreme Obesity": 5
    }

    myframe['Index']=[map[i] for i in myframe['Index']]

    #print(myframe)
    myframe['Male']=0
    myframe['Female']=0

    instance=0
    for i in myframe['Gender']:
        if(i=="Male"):
            myframe.at[instance, 'Male'] = 1
        if(i=="Female"):
            myframe.at[instance, 'Female'] = 1
        instance=instance+1

    #print(myframe)

    myframe=myframe.drop(['Gender'], axis=1)
    #print(myframe)
    myframe=myframe.iloc[:,[3,4,0,1,2]]
    #print(myframe)
    myframe.to_csv('E:\\Sharanya\\pythonnewvsc\\Finaldataset_BMI_output2.csv', index=False)

    myframe['distance']=0
    testvector=[1,0,142,131]
    for i in range(0,368):
        instance_vector = myframe.iloc[i, :4]
        distance_value=euciladean(testvector,instance_vector,4)
        myframe.at[i, 'distance'] = distance_value

    #print(myframe)
    sorted_myframe = myframe.sort_values(by='distance', ascending=True).reset_index(drop=True)
    #print(sorted_myframe)


    k=5
    sum_list=[0,0,0,0,0,0]
    in_no=0
    sum=0
    for i in map.values():
        sum=0
        for j in range(0,k):
            if(i==sorted_myframe.loc[j, 'Index']):
                sum=sum+1
        sum_list[in_no]=sum
        in_no=in_no+1

    #print(sum_list)
    max=0
    for i in range(0,6):
        if(sum_list[i]>=max):
            max=sum_list[i]
            position=i


    #print(position)

    for i in map.keys():
        if(map[i]==position):
            predicted_target=i

    #print(predicted_target)
    return(predicted_target)
        
        
print("predicted BMI is=",knnclassifer_sharanya())
               
