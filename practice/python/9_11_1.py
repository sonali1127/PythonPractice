class Solution:
    def isHappy(self, n: int) -> bool:
        while n>9:
            s=0
            while n!=0:
                r=n%10
                s=s+r**2
                n=n//10
            n=s
        if n==1 or n==7 :
            return 1
        return 0
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        ob = Solution()
        print(ob.isHappy(N))