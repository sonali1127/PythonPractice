'''ass3:write a program to find second minimum from the list'''
def smin(l):
    minn=l[0]
    for i in l:
        if i<minn:
            minn=i
    return minn
n=int(input())
l=list(map(int,input().split()))
fmin=smin(l)
l.remove(fmin)
sminimum=smin(l)
print(sminimum)
print(l)