'''In a small village, people celebrate their happiness by performing a ritual with numbers. A
number is considered "happy" if the process of repeatedly summing the squares of its digits
eventually leads to 1. For example, the number 19 is happy because 1^2+ 9^2 = 82, 8^2 + 2^2=
68, and so on, eventually reaching 1. Your task is to find all happy numbers in a given range.
Can you help the villagers find their happy numbers?
Constraints:
● The range is between 1 and 10^4.
Sample Input:
1, 20
Sample Output:
[1, 7, 10, 13, 19]
Explanation:
The happy numbers between 1 and 20 are 1, 7, 10, 13, and 19.'''
def happy(n):
    while(n>9):
        s=0
        while(n!=0):
            r=n%10
            s=s+r**2
            n=n//10
        n=s
    return n
a=int(input())
b=int(input())
for i in range(a,b+1):
    if happy(i)==1 or i==7:
        print(i,end=" ")
