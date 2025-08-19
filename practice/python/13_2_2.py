#write a program to print given year is leap year or not
class Solution:
    def leap(self,y):
        if ((y%4==0 and y%100!=0) or y%400==0):
            return True
        else:
            return False
ob=Solution()
y=int(input())
if ob.leap(y):
    print("leap year")
else:
    print("Not a leap year")