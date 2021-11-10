import math
a= int(input())
b= int (input())
k=0
if (a!=b):
    for i in range (a+1,(b)):
        p=0
        c=int(math.sqrt(i))
        for j in range (2,c+1):
            if (i%j == 0):
                p=1
                break
        if (p==0 and i !=1 and k==0):
            print (i,end="")
            k+=1
        elif (p==0 and i!=1 ):
            print(","+str(i),end="")

