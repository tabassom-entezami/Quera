def ans(n,k):
    ans1=1
    ans2=1
    ans3=0
    ans4=1
    for i in range (1,n+1):
        ans1*=i
    for i in range (1 ,k+1):
        ans2*=i
    for i in range (1,n-k+1):
        ans4*=i
    ans3=ans1/(ans2*ans4)
    return(int(ans3))

n = int(input())
for i in range (0,n):
    for j in range (0,i+1):
        print (ans(i,j)," ",end="")
    print()
