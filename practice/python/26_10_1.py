'''ass1:
    write a program to print given number is palindrome or not
    input:123
    output:not a palindrome
    input:12121
    output:palindrome
'''
n=int(input('enter n value:'))
temp=n
res=0
while n!=0:
    r=n%10
    res=res*10+r
    n=n//10
if res==temp:
    print("palindrome")
else:
    print("not a palindrome")