#write a program to print given number is armstrong number or not
n=int(input())
temp=n
res=0
while(n!=0):
    r=n%10
    res=res+r**3
    n=n//10
if temp==res:
    print("Armstrong Number")    
else:
    print("Not a Armstrong Number")    