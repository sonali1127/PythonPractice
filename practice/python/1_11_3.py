'''ass3:write a program to print difference of maximum value and minimum value
using exisition functions
input:
    5
    1
    3
    4
    6
    2
output:5(max is 6 and min is 1,difference is 6-1=5)'''
n=int(input())
l=[]
for i in range(n):
    a=int(input())
    l.append(a)
print(max(l)-min(l))