'''ass1:
write a program to print 1 to n odd numbers
input:10
output: 1 3 5 7 9'''
n=int(input())
for i in range(1,n+1,2):
    print(i,end=' ')