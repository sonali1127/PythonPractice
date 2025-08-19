'''ass1:wap to separate even numbers oneside and odd numbers another side
ex:input:6
        5 4 9 3 51 2
output:4 2 5 9 3 51'''
n=int(input())
l=list(map(int,input().split()))
even=[]
odd=[]
for i in l:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
even.extend(odd)
for i in even:
    print(i,end=' ')