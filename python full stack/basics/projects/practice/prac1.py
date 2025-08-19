'''Problem Statement:
In a distant kingdom, a wise king has a chest full of magical numbers. He decides to reward the
most observant mathematician in the land. Your task is to analyze a list of these numbers and
identify which ones contain an even number of digits. The king believes that only numbers with
an even number of digits hold the key to unlock the hidden treasures of the kingdom. Can you
help identify these numbers for the king?
Constraints:
● The array length 1≤n≤10^4
● Each number in the array is a positive integer 1≤num≤10^9
Sample Input:
123,4567,89,1001,22
Sample Output:
4567, 89, 1001, 22
Explanation:
Numbers like 123 have 3 digits, which is odd, so they are excluded. However, 89 and 22 have 2
digits, which is even, so they are included.

n=list(map(int,input().split()))
for i in n:
    c=0
    temp=i
    while(i!=0):
        r=i%10
        c=c+1
        i=i//10
    if c%2==0:
        print(temp,end=" ")
    '''
l=list(map(int,input().split()))
for i in l:
    i=str(i)
    n=len(i)
    if n%2==0:
        print(i,end=" ")