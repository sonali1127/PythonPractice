'''ass2:wap to print duplicate elements from the list
ex:input:6
        1 2 1 4 5 2
output:1 2'''
n=int(input())
l=list(map(int,input().split()))
for i in range(0,n):
    count=0
    for j in range(i,n):
        if l[i]==l[j]:
            count=count+1
    if count>1:
        print(l[i],end=' ')
        
