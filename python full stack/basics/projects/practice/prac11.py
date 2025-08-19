'''Alice and Bob each created a challenge. These challenges are scored based on three
categories: clarity, originality, and difficulty. The scores for Alice's challenge are given as a =
[a[0], a[1], a[2]], and the scores for Bob's challenge are given as b = [b[0], b[1],
b[2]].
Task:
Compare their scores category by category:
1. If a[i] > b[i], Alice earns 1 point.
2. If a[i] < b[i], Bob earns 1 point.
3. If a[i] == b[i], no points are awarded.
You need to calculate the total points for Alice and Bob and return them as [Alice's score,
Bob's score].
Input:
● a: A list of 3 integers representing Alice's scores.
● b: A list of 3 integers representing Bob's scores.
Output:
● A list [Alice's score, Bob's score].
'''
s=list(map(int,input().split()))
n=list(map(int,input().split()))
a=b=0
for i in range(0,len(s)):
    if s[i]>n[i]:
        a=a+1
    elif s[i]==n[i]:
        pass
    else:
        b=b+1
print(a,b)