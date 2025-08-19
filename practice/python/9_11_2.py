#User function Template for python3
class Solution:
    def isHappy (self, N):
        while N>9:
            s=0
            while N!=0:
                r=N%10
                s=s+r**2
                N=N//10
            N=s
        if N==1 or N==7 :
            return 1
        return 0
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        ob = Solution()
        print(ob.isHappy(N))
