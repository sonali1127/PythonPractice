#write a program to print given number is prime or not
n=int(input())
f=0
for i in range(1,n+1):
    if(n%i)==0:
        f=f+1
if f==2:
    print("prime number")
else:
    print("Not a prime number")