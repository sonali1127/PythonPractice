'''#ass2:wap to print count of leap years in the given range
input:2000 2010
output:3'''
def leap(y):
    if y%400==0 or y%4==0 and y%100!=0:
        return True
    else:
        return False
s,e=map(int,input().split())
l=[i for i in range(s,e+1) if(leap(i))]
print(len(l))