class Solution:
    def romanToDecimal(self, S): 
        # code here
        r={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        S=S.replace("IV","IIII")
        S=S.replace("IX","VIIII")
        S=S.replace("XL","XXXX")
        S=S.replace("XC","LXXXX")
        S=S.replace("CD","CCCC")
        S=S.replace("CM","DCCCC")
        sum=0
        for i in S:
            sum=sum+r[i]
        return sum
if __name__=='__main__':
    t = int(input())
    for _ in range(t):
        ob = Solution()
        S = input()
        print(ob.romanToDecimal(S))