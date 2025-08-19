'''write a program to print biggest of three numbers
input:4 5 2
output:5'''
a,b,c=map(int,input('enter 3 numbers:').split())
print(max(max(a,b),c))
