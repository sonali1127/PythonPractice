class Solution:
    def missingNumber(self,array,n):
        osum=n*(n+1)//2
        asum=0
        for i in array:
            asum=asum+i
        return osum-asum
t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=Solution().missingNumber(a,n)
    print(s)
