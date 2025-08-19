'''ass1:wap to print 1 to n armstrong numbers using list comprehension
input:400
output:1 153 371'''
def armstrong(n):
    res=0
    temp=n
    while(n!=0):
        r=n%10
        res=res+r**3
        n=n//10
    if temp==res:
        return res
n=int(input())
l=[i for i in range(1,n+1) if(armstrong(i))]
for i in l:
    print(i,end=' ')