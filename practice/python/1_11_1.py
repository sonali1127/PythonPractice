'''ass1:
write a program to store n values into list and print first and last value
input:
3
1
4
7
output:
1
7'''
n=int(input())
l=[]
for i in range(n):
    a=int(input())
    l.append(a)
print(l[0])
print(l[-1])