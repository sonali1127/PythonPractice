def prime(n):
    if n<1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
sum=0
for i in range(5):
    n=int(input())
    if prime(n):
        sum+=n
    else:
        n=int(input())
print(sum)