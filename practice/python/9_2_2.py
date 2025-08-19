#wap to print given number is palindrome or not
def palindrome(n):
    res=0
    while(n!=0):
        r=n%10
        res=res*10+r
        n=n//10
    return res
n=int(input())
num=n
if palindrome(n)==num:
    print("palindrome")
else:
    print("not a palindrome")