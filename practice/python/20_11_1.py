'''ass1:wap to print duplicate count of the list
ex:input:6
        1 2 1 2 1 2
output:4'''
n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(0,n):
    count=0
    for j in range(i,n):
        if l[i]==l[j]:
            count=count+1
    if count>1:
        c=c+1
print(c)