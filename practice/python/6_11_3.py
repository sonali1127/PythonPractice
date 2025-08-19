'''ass3:
    write a program to print prime count upto given range
input:
    6
output:
    3(2,3,5)'''
m=int(input())
count=0
for n in range(1,m+1):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c=c+1
    if c==2:
        count=count+1
print(count)