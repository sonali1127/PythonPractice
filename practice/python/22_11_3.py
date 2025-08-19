'''#assignment3:write a program to separate list using list slicing
ex: 0 1 2 3 4 5 6  7  8  9
    1 5 6 7 8 9 10 14 78 15
    2 5-first part
    6 7-second part
output:6 7 8 9 10 14'''
l=list(map(int,input().split()))
m=l[2:6]+l[6:8]
for i in m:
    print(i,end=' ')