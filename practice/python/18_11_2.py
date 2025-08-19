n=int(input())
l=list(map(int,input().split()))
m=list(map(int,input().split()))
s=[]
for i in range(n):
    res=l[i]+m[i]
    s.append(res)
minn=s[0]   
for i in s:
    if i<minn:
         minn=i
print(minn)      