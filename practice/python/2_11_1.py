'''Finding minimum value from the list'''
n=int(input())
l=list(map(int,input().split()))
minn=l[0]
for i in l:
    if i<minn:
        minn=i
print(minn)