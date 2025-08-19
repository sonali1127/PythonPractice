'''ass1:wap to print n prime numbers using list comprehension
input:5
output:2 3 5'''
def prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
n=int(input())
l=[i for i in range(1,n+1) if prime(i)]
for i in l:
    print(i,end=' ')