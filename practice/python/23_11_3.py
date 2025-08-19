'''ass3:wap to print elements in order within specified interval in descending order
input:8
    12 45 85 96 2 0 4 9
    3 6
output: 
    0  1  2  3   4  5  6   7
    12 45 85 96  4  2  0  9'''
n=int(input())
l=list(map(int,input().split()))
s,e=map(int,input().split())
first=l[0:s]
req=l[s:e+1]
last=l[e+1:n]
req.sort(reverse=True)
res=first+req+last
for i in res:
    print(i,end=' ')