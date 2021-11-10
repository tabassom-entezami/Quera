a=[1,2,3,4]
a[0],a[1],a[2],a[3] = map (int , input().split())

b=[0,0,0,0]
i=0
j=0
while (a[0] > 0 and a[2]>0):
    a[i]-=1
    if (i == 0):
        i+=2
    elif (i == 2):
        i-=2
    b[j]=b[j]+1
    if(j<3):
        j+=1
    else :
        j=0

for i in range (0,4):
    print (b[i],end=" ")
