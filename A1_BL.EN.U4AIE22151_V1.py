import sys
class assignment1:
    def PairOfElements(list1):
        sum=0
        count=0
        for i in range(0,6): #loop goes through all the alphabets
            #print(list1[i])
            for j in range(i,6): #loop goes through all the alphabets that hasnt been checked
                #print(list1[j])
                if((list1[i]+list1[j])==10): #checks for sum of 10
                    #print(list1[i],"and",list1[j])
                    count=count+1 #adds 1  to counter
        return count

    def rangeFind(list2):
        max=-sys.maxsize #assigns negative infinite value to max
        min=sys.maxsize #assigns positive infinitie value to min
        for i in range(0,len(list2)):
            if(list2[i]>=max):
                max=list2[i] # if a higher value than in the variable is found then it is stored
            if(list2[i]<=min):
                min=list2[i] # if a lower value than in the variable is found then it is stored
        return (max-min) #returns range

    def matrixmulti(matrix,n):
        
        multi=[]
        x=0
        for i in range(0,n):
            row=[]
            for j in range(0,n):
                x=0
                for k in range(0,n):
                    x=x+matrix[i][k]*matrix[k][j] #multiplies appropriate elements and stores in x
                row.append(x) # the elemt x i appended to the row list
            multi.append(row) #the row list is appended to multi matrix
                           

        return multi
                    

    def word_count(word):
        list3=[]
        max_count=0
        for i in word: #iterates through each character in the word
            count=0
            for j in word: #iterates through each character in the word
                if(i==j): #if the letter is matched then count is incremented by 1
                    count=count+1
            if(count>=max_count):
                max_count=count # the max count stores the count variable when a higher count is found max_count is updated
                maxletter=i #the corresponding letter to the max_count at every instant is saved in maxletter
                
        return max_count, maxletter


    #main
    #Options of the questions available
    print("1.Program to count pairs of elements with sum equal to 10.")
    print("2.Program that takes a list of real numbers as input and returns the range (difference between minimum and maximum) of the list.")
    print("3.Program that accepts a square matrix A and a positive integer m as arguments and returns A^m")
    print("4.Program to count the highest occurring character & its occurrence count in an input string.")
    choice=int(input("Enter your choice of question:"))  #saves choice of user
    if(choice==1):
        list_input=[]
        n=int(input("Enter length of list")) #accepts stores length of list
        print("Enter list of numbers:")
        for i in range(0,n): #stores the input numbers in coressponding locations
                a=int(input())
                list_input.append(a)
        print("Number of pairs=",PairOfElements(list_input)) #number of pairs are printed
    elif(choice==2):
        n=int(input("Enter length of list")) #accepts stores length of list
        if(n>=3): #checks if length is more than 3 then accepts the numbers
            list_input=[]
            print("Enter list of numbers:")
            for i in range(0,n): #stores the input numbers in coressponding locations
                a=int(input())
                list_input.append(a)
            for i in range(0,n):
                print(list_input[i])
            print("Range=",rangeFind(list_input)) #range is printed
        else:
            print("range insufficient")
        
    elif(choice==3):
        matrix_input=[]
        n=int(input("Enter order of matrix:")) #order of matrix accepted and stored
        element_no=1
        for i in range(0,n):
            row=[]
            for j in range(0,n):
                print("Enter number ",element_no,":") #stores the input numbers in coressponding locations
                element_no=element_no+1
                row.append(int(input())) #list to store each row elements
            matrix_input.append(row) #appends rows to the matrix
                    

        m = int(input("Enter the power to raise the matrix to: "))
        for i in range(m - 1):
            matrix_input = matrixmulti(matrix_input, n) #calls function m times to multiply same matrix with power m

        for i in range(0,n):
                for j in range(0,n):
                    print(matrix_input[i][j],end = " ")
                print()

    elif(choice==4):
        word_input=input("Enter your string") #accepts and stores the string
        t=word_count(word_input)
        print(t[1]," occurs the most :",t[0]," times") # prints the alphabet and number of times it occurs by using the returned tuple

    else:
        print("invalid input") #if an option except 1,2,3,and 4 is inputed then invalid input is displayed because there are only 4 questions
                                

        
