#ass1:
#wap to print sum of each column values
n=int(input())
A=[]
for i in range(n):
    l=list(map(int,input().split()))
    A.append(l)
for i in range(0,n):
    rsum=0
    for j in range(0,n):
        rsum=rsum+A[j][i]
    print(rsum,end=' ')
