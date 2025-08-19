n=int(input())
l=list(map(int,input().split()))
m=list(map(int,input().split()))
for i in range(n):
    res=l[i]-m[i]
    print(res,end=' ')