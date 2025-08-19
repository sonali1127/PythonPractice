a=list(map(int,input().split()))
b=[]
for i in a:
    n=i-min(a)
    if n!=0:
        b.append(n)
        
