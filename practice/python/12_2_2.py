#write a program to print given number is armstrong number or not(class)
class Solution:
    def armstrong(self,n):
        res=0
        temp=n
        while(temp!=0):
            r=temp%10
            res=res+r**3
            temp=temp//10
        return res
ob=Solution()
n=int(input())
if ob.armstrong(n)==n:
    print("Yes")
else:
    print("No")