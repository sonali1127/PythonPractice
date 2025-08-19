'''ass1:
    write a program to merge two list and find the minimum value from the list'''
n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))
a.extend(b)
minn=a[0]
for i in a:
    if i<minn:
        minn=i
print(minn)