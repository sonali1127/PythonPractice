""""
28
1 2 4 7 14 28
"""
n=int(input())
for i in range(1,n+1):
    if n%i==0:
        print(i,end=" ")