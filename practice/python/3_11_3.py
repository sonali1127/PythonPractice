'''ass3:
    write a program to print maximum and minimum values from the list'''
n=int(input())
l=list(map(int,input().split()))
minn=maxx=l[0]
for i in l:
    if i>maxx:
        maxx=i
    if i<minn:
        minn=i
print('min:',minn,' max:',maxx)