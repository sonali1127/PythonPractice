'''ass2:
    write a program to update values at given positions
    4
    1
    2
    8
    9
    1
    2
    output:
        1 2 8 9'''
n=int(input())
l=[]
for i in range(n):
    a=int(input())
    l.append(a)
x=int(input())
data=int(input())
l[x]=data
print(l)