from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        osum=n*(n+1)//2
        asum=0
        for i in nums:
            asum=asum+i
        return osum-asum
t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=Solution().missingNumber(a)
    print(s)