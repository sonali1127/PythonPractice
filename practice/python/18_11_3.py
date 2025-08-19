l=list(map(int,input().split()))
m=list(map(int,input().split()))
l.extend(m)
minn=l[0]
for i in l:
    if i<minn:
        minn=i
print(minn)