import math
class eucliadean_manhattan_distance:
    def euciladean(vector1,vector2,n):
        sum=0
        for i in range(0,n):
            sum=sum+(vector2[i]-vector1[i])**2
        print(sum)
        return(math.sqrt(sum))
    
    def manhattan(vector1,vector2,n):
        sum=0
        for i in range(0,n):
            print(vector2[i]," ",vector1[i])
            sum=sum+abs(vector2[i]-vector1[i])
        return(sum)
        

    #main
    vector1_para=[]
    vector2_para=[]
    m=int(input("Enter length of vector"))
    print("Enter entries of first vector")
    for i in range(0,m):
        value_v1=int(input())
        vector1_para.append(value_v1)

    print("Enter entries of second vector")    
    for i in range(0,m):
        value_v2=int(input())
        vector2_para.append(value_v2)

    print("1.Eucildean Distance")
    print("2.Manhattan Distance")
    choice=int(input("Enter your choice"))
    if(choice==1):
        print(vector1_para,vector2_para,m)
    elif(choice==2):
       print(vector1_para,vector2_para,m)