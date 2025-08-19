'''ass2:
 write a program to print * traingle series using n value
input:
n=4
output:
*
* *
* * *
* * * *'''
n=int(input("n="))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=' ')
    print()