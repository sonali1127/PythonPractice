#write a program to print given number is palindrome number or not
n=int(input())
temp=n
res=0
while(n!=0):
    r=n%10
    res=res*10+r
    n=n//10
if temp==res:
    print("Palindrome")    
else:
    print("Not a Palindrome")    