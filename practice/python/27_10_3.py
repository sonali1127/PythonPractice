'''ass3:
write a program to print given number is prime or not using for loop
input:5
output:yes
input:6
output:no'''
n=int(input())
c=0
for i in range(1,n+1):
    if n%i==0:
        c=c+1
if c==2:
    print('yes')
else:
    print('no')