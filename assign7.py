for i in range(7,0,-1):
    for k in range(i,7):
        print(" ",end="")
    for j in range(i):
        if(j==0 or j==i-1):
            print(i,end=" ")
        else:
           if(i==7):
               print(i,end=" ")
           else:    
               print(" ",end=" ")
               
    print("") 
