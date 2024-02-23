import pandas as pd
import numpy as np
import statistics
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
class lab4:

    def lab4questions():
        df=pd.read_csv("E:\\Sharanya\\MLsem4\\projectdatasetML.csv",skiprows=86)
        
        
        columnsdrop = ["kepler_name", "koi_comment", "koi_longp", "koi_model_dof", "koi_model_chisq", "koi_sage", "koi_ingress", "kepoi_name", "koi_vet_date", "koi_limbdark_mod", "koi_parm_prov", "koi_tce_delivname", "koi_sparprov", "koi_datalink_dvr", "koi_datalink_dvs", "koi_quarters"]

        
        df.drop(columns=columnsdrop,inplace=True)

        print(df)

        pd.set_option('display.max_columns', None)
        print(df.head())

        labelencoded=LabelEncoder()

        df['koi_disposition']=labelencoded.fit_transform(df['koi_disposition']) #label encoding of all categorical columns
        df['koi_vet_stat']=labelencoded.fit_transform(df['koi_vet_stat'])
        df['koi_pdisposition']=labelencoded.fit_transform(df['koi_pdisposition'])
        df['koi_disp_prov']=labelencoded.fit_transform(df['koi_disp_prov'])
        df['koi_fittype']=labelencoded.fit_transform(df['koi_fittype'])
        df['koi_trans_mod']=labelencoded.fit_transform(df['koi_trans_mod'])

        print(df)

        for column_name, dtype in df.dtypes.items():
            print(f"Column '{column_name}' has data type '{dtype}'.")
        print("------------------------------------") #searching for which coumns have missing values
        null_columns = df.isnull().any()

        for column_name, has_null in null_columns.items():
            if(has_null==True):
                print(column_name, has_null)

        #print(null_columns)
        
        for column_name, has_null in null_columns.items():
            if(has_null==True):
                print(column_name, has_null)
                instance=0
                for i in df[column_name]:
                    if pd.isnull(i):
                        df.at[instance, column_name] = df[column_name].mean()
                    instance=instance+1
                        
        print(df)

        print("--------------------------------------") 

        null_columns = df.isnull().any()
        for column_name, has_null in null_columns.items():
            if(has_null==True):
                print(column_name, has_null)

        df.to_csv('E:\\Sharanya\\MLsem4\\correctedfile.csv', index=False)

        feat_vecs=df.iloc[:,:-1]
        classlabels=df.iloc[:,2]

        uniqueclass=np.unique(classlabels)

        print(feat_vecs)


        instance=0 #replacing missing values with mean
        classmeanlist=[]
        classstdlist=[]
        for i in range(len(feat_vecs)):
            classspecificvector = []
            for j in uniqueclass:
                if classlabels[i] == j:  # 
                    classspecificvector.append(feat_vecs.iloc[i])
        classmean = np.mean(classspecificvector, axis=0)
        classstd =np.std(classspecificvector, axis=0)
        classmeanlist.append(classmean)
        classstdlist.append(classstd)


        print(classmeanlist)
        print(classstd)

        for i in classmeanlist:
            for j in classmeanlist:
                print(np.linalg.norm(i - j))

        
        selectedcol=df['koi_hmag'] #plotting histogram for one column
        h,e=np.histogram(selectedcol,bins=10)

        plt.hist(selectedcol,bins=e, edgecolor='black')
        plt.xlabel('hmag')
        plt.ylabel('Freq')
        plt.show

        from sklearn.model_selection import train_test_split 
        print(classlabels)
        classlabels
        X_train,X_test,y_train,y_test=train_test_split(feat_vecs,classlabels,test_size=0.3)
    
        from sklearn.neighbors import KNeighborsClassifier #performing knn classification for 3 k 
        neigh=KNeighborsClassifier(n_neighbors=3)
        neigh.fit(feat_vecs,classlabels)
        print(neigh.score(X_test,y_test))

        predict=neigh.predict(X_test)

        from sklearn.metrics import accuracy_score
        print(accuracy_score(y_test,predict))

        plt.figure()
        accu=[]
        k_values = np.arange(1, 12, 1) #performing knn for 1 to 11 k values
        for k in range(1,12):
            print("for k=",k)
            neigh=KNeighborsClassifier(n_neighbors=k)
            neigh.fit(feat_vecs,classlabels)
            print(neigh.score(X_test,y_test))

            predict=neigh.predict(X_test)

            accu.append(accuracy_score(y_test,predict))
            print(accuracy_score(y_test,predict)) #finding accuracy

        plt.plot(k_values, accu, marker='o', linestyle='-')
        plt.xlabel('k')
        plt.ylabel('Accuracy') #plotting accuracy for all k
        plt.show()

        plt.figure()
        from sklearn.metrics import confusion_matrix
        cm = confusion_matrix(y_test, predict)


        plt.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
        plt.title('Confusion matrix') #finidng confusion matrix
        plt.colorbar()
        plt.xlabel('Predicted')
        plt.ylabel('True')
        plt.show()
        plt.show()


        neigh=KNeighborsClassifier(n_neighbors=3)
        neigh.fit(feat_vecs,classlabels)
        #print(neigh.score(X_test,y_test))

        predict=neigh.predict(X_test)

        from sklearn.metrics import accuracy_score
        #print(accuracy_score(y_test,predict))
        from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score
        precision = precision_score(y_test, predict, average='macro')
        recall = recall_score(y_test, predict, average='macro')
        f1 = f1_score(y_test, predict, average='macro')

        print("Precision:", precision) #generating report for k=3
        print("Recall:", recall)
        print("F1-score:", f1)
    lab4questions()
