#ass2:wap to print given num is prime or not using normal approach
def isprime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
n=int(input("enter a number:"))
if isprime(n):
    print("prime number")
else:
    print("not a prime number")
    