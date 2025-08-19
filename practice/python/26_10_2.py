'''write a program to print given number is armstrong number or not
input:
153
output:armstrong'''
n=int(input('enter n value:'))
temp=n
res=0
while n!=0:
    r=n%10
    res=res+r**3
    n=n//10
if temp==res:
    print("armstrong")
else:
    print("not a armstrong")
# model:2
n=int(input("enter a value:"))
t=temp=n
i=res=0
while n!=0:
    i=i+1
    n=n//10
while t!=0:
    r=t%10
    res=res+r**i
    t=t//10
if temp==res:
    print("armstrong")
else:
    print("not a armstrong")