'''ass3:wap to store odd numbers in the list using list comprehension
input:10
output:1 3 5 7 9'''
n=int(input())
l=[i for i in range(1,n+1) if(i%2!=0)]
for i in l:
    print(i,end=' ')